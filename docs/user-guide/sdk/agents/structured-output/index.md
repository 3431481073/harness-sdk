An agent answers in text, which works when a person reads it. When your code needs to act on the answer, text is hard to parse. Structured output returns an object instead. You describe the fields you need in a schema, and the agent returns an object with those fields, validated against the schema.

A schema lists each field’s name, type, and description. In Python, write it as a [Pydantic model](https://docs.pydantic.dev/latest/concepts/models/), which installs with `strands-agents`. In TypeScript, write it as a [Zod schema](https://zod.dev/) and install Zod with `npm install zod`.

## Request structured output

This agent reads a customer support message and returns the category, priority, and summary that your code needs to route the ticket:

(( tab "Python" ))
```python
from typing import Literal

from pydantic import BaseModel, Field
from strands import Agent
from strands.types.exceptions import StructuredOutputException


class TicketTriage(BaseModel):
    """Routing decision for one customer support message."""

    category: Literal["billing", "bug", "account", "other"] = Field(
        description="The team that should handle the message"
    )
    priority: Literal["low", "medium", "high"] = Field(
        description="high when the customer is blocked or losing money"
    )
    summary: str = Field(description="One sentence describing the problem")


def triage(message: str) -> TicketTriage:
    # A fresh agent per message keeps tickets from sharing conversation history
    agent = Agent(callback_handler=None)
    try:
        result = agent(message, structured_output_model=TicketTriage)
    except StructuredOutputException:
        # Send anything the agent can't classify to a person
        return TicketTriage(category="other", priority="medium", summary=message)
    return result.structured_output


ticket = triage("I was charged twice this month and need one of the charges refunded.")
print(f"{ticket.priority} | {ticket.category} | {ticket.summary}")
```

`invoke_async` takes the same argument.
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent, StructuredOutputError } from '@strands-agents/sdk'
import { z } from 'zod'

const TicketTriageSchema = z
  .object({
    category: z
      .enum(['billing', 'bug', 'account', 'other'])
      .describe('The team that should handle the message'),
    priority: z
      .enum(['low', 'medium', 'high'])
      .describe('high when the customer is blocked or losing money'),
    summary: z.string().describe('One sentence describing the problem'),
  })
  .describe('Routing decision for one customer support message')

type TicketTriage = z.infer<typeof TicketTriageSchema>

async function triage(message: string): Promise<TicketTriage> {
  // A fresh agent per message keeps tickets from sharing conversation history
  const agent = new Agent({ printer: false })
  try {
    const result = await agent.invoke(message, {
      structuredOutputSchema: TicketTriageSchema,
    })
    return result.structuredOutput as TicketTriage
  } catch (error) {
    if (error instanceof StructuredOutputError) {
      // Send anything the agent can't classify to a person
      return { category: 'other', priority: 'medium', summary: message }
    }
    throw error
  }
}

const ticket = await triage(
  'I was charged twice this month and need one of the charges refunded.'
)
console.log(`${ticket.priority} | ${ticket.category} | ${ticket.summary}`)
```
(( /tab "TypeScript" ))

Typical output:

```plaintext
high | billing | Customer was charged twice this month and is requesting a refund.
```

`TicketTriage` lists the fields the routing code needs. `category` and `priority` accept only fixed values, so the agent can only pick a team and a priority you’ve defined. The model reads each field description, so describe what a field means, not only its type.

Pass the schema as `structured_output_model``structuredOutputSchema` and read the object from `result.structured_output``result.structuredOutput`. In Python, the object is an instance of your model. In TypeScript, cast it to the `z.infer` type.

If the agent doesn’t return an object, the call raises `StructuredOutputException``StructuredOutputError`. `triage` catches it and returns a ticket in the `other` category for a person to review.

Invalid field values don’t raise. Strands sends the validation errors back to the agent, and the agent corrects them.

## Use tools

The agent can call tools before it returns the object. Here, it looks up the customer’s name and plan by email:

(( tab "Python" ))
```python
from typing import Literal

from pydantic import BaseModel
from strands import Agent, tool


@tool
def lookup_customer(email: str) -> dict:
    """Look up a customer's name and plan by email address."""
    customers = {"dana@example.com": {"name": "Dana Ruiz", "plan": "enterprise"}}
    return customers.get(email, {"name": "unknown", "plan": "free"})


class CustomerTicket(BaseModel):
    customer_name: str
    plan: Literal["free", "pro", "enterprise"]
    priority: Literal["low", "medium", "high"]


agent = Agent(tools=[lookup_customer], callback_handler=None)
result = agent(
    "From dana@example.com: our dashboard has been down for an hour.",
    structured_output_model=CustomerTicket,
)
print(result.structured_output)
```

Typical output:

```plaintext
customer_name='Dana Ruiz' plan='enterprise' priority='high'
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent, tool } from '@strands-agents/sdk'
import { z } from 'zod'

const customers: Record<string, { name: string; plan: string }> = {
  'dana@example.com': { name: 'Dana Ruiz', plan: 'enterprise' },
}

const lookupCustomer = tool({
  name: 'lookup_customer',
  description: "Look up a customer's name and plan by email address.",
  inputSchema: z.object({ email: z.string() }),
  callback: ({ email }) => customers[email] ?? { name: 'unknown', plan: 'free' },
})

const CustomerTicketSchema = z.object({
  customerName: z.string(),
  plan: z.enum(['free', 'pro', 'enterprise']),
  priority: z.enum(['low', 'medium', 'high']),
})

const agent = new Agent({ tools: [lookupCustomer], printer: false })
const result = await agent.invoke(
  'From dana@example.com: our dashboard has been down for an hour.',
  { structuredOutputSchema: CustomerTicketSchema }
)
console.log(result.structuredOutput)
```

Typical output:

```plaintext
{ customerName: 'Dana Ruiz', plan: 'enterprise', priority: 'high' }
```
(( /tab "TypeScript" ))

## Extract from a conversation

A schema applies only to the call that passes it, so earlier turns return text as usual. The agent fills the fields from the whole conversation:

(( tab "Python" ))
```python
from pydantic import BaseModel
from strands import Agent


class Escalation(BaseModel):
    problem: str
    steps_tried: list[str]


agent = Agent(callback_handler=None)
agent("Hi, I can't log in to my account.")
agent("I reset my password twice, and the reset email never arrives.")

result = agent(
    "Summarize this conversation for the escalation team.",
    structured_output_model=Escalation,
)
escalation = result.structured_output
print(escalation.problem)
for step in escalation.steps_tried:
    print(f"- {step}")
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent } from '@strands-agents/sdk'
import { z } from 'zod'

const EscalationSchema = z.object({
  problem: z.string(),
  stepsTried: z.array(z.string()),
})

const agent = new Agent({ printer: false })
await agent.invoke("Hi, I can't log in to my account.")
await agent.invoke('I reset my password twice, and the reset email never arrives.')

const result = await agent.invoke(
  'Summarize this conversation for the escalation team.',
  { structuredOutputSchema: EscalationSchema }
)
const escalation = result.structuredOutput as z.infer<typeof EscalationSchema>
console.log(escalation.problem)
for (const step of escalation.stepsTried) {
  console.log(`- ${step}`)
}
```
(( /tab "TypeScript" ))

Typical output:

```plaintext
The user is unable to log in and is not receiving password reset emails.
- User reset their password twice but never received the reset email.
- Agent suggested checking the spam folder for the reset email.
```

## Stream the response

Pass the schema to a stream the same way. Text arrives in chunks as the model writes it, and the object arrives once, on the final result:

(( tab "Python" ))
```python
import asyncio

from pydantic import BaseModel
from strands import Agent


class ReplyDraft(BaseModel):
    subject: str
    body: str


async def main():
    agent = Agent(callback_handler=None)
    async for event in agent.stream_async(
        "Draft a reply apologizing for a delayed refund.",
        structured_output_model=ReplyDraft,
    ):
        if "data" in event:
            print(event["data"], end="", flush=True)
        elif "result" in event:
            draft = event["result"].structured_output
            print(f"\nSubject: {draft.subject}")


asyncio.run(main())
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent } from '@strands-agents/sdk'
import { z } from 'zod'

const ReplyDraftSchema = z.object({
  subject: z.string(),
  body: z.string(),
})

type ReplyDraft = z.infer<typeof ReplyDraftSchema>

const agent = new Agent({ printer: false })
const stream = agent.stream('Draft a reply apologizing for a delayed refund.', {
  structuredOutputSchema: ReplyDraftSchema,
})

for await (const event of stream) {
  if (
    event.type === 'modelStreamUpdateEvent' &&
    event.event.type === 'modelContentBlockDeltaEvent' &&
    event.event.delta.type === 'textDelta'
  ) {
    process.stdout.write(event.event.delta.text)
  } else if (event.type === 'agentResultEvent') {
    const draft = event.result.structuredOutput as ReplyDraft
    console.log(`\nSubject: ${draft.subject}`)
  }
}
```
(( /tab "TypeScript" ))

Typical output:

```plaintext
I'd be happy to help draft a reply apologizing for a delayed refund!
Subject: Apology for Your Delayed Refund
```

## Next steps

-   [Structured output](/docs/user-guide/sdk/agents/structured-output-behavior/index.md): agent-level schemas, how a schema becomes a tool, validation retries, and errors.
-   [Stream responses](/docs/user-guide/sdk/streaming/index.md): every event type a stream carries.
-   [Create custom tools](/docs/user-guide/sdk/tools/custom-tools/index.md): write tools like `lookup_customer`.

## Related pages

- [LiteLLM](/docs/user-guide/sdk/model-providers/litellm/index.md) (1 shared tag)
- [Structured output similarity evaluator](/docs/user-guide/evals-sdk/evaluators/structured_output_evaluator/index.md) (1 shared tag)
- [Structured output](/docs/user-guide/sdk/agents/structured-output-behavior/index.md) (1 shared tag)
- [OpenAI](/docs/user-guide/sdk/model-providers/openai/index.md) (1 shared tag)
- [Writer](/docs/user-guide/sdk/model-providers/writer/index.md) (1 shared tag)
- [Anthropic](/docs/user-guide/sdk/model-providers/anthropic/index.md) (1 shared tag)


## Implementation

### Python

- [harness-sdk/strands-py/src/strands/agent/agent.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/agent/agent.py)

### TypeScript

- [harness-sdk/strands-ts/src/agent/agent.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts)
