An agent in production takes untrusted input, calls tools with real permissions, and returns model output to real users. Securing it means putting controls at each of those boundaries: screen what goes in and out with guardrails, write system prompts that hold up against injection, treat any history you did not produce as untrusted, and keep personal data out of your telemetry. The agent you built does not change; you wrap it in the safeguards production demands.

## Safeguards

[Add guardrails](guardrails/index.md)Filter harmful content, block off-topic requests, and protect sensitive data at the model boundary.

[Harden your prompts](prompt-engineering/index.md)Write system prompts that resist injection, sanitize input, and keep the agent in scope.

[Trust your message history](trusted-message-history/index.md)Treat history from a source you do not control as untrusted, and clear forged tool content.

[Redact PII](pii-redaction/index.md)Keep personal data out of traces and logs with library or collector-level masking.

[Build responsibly](responsible-ai/index.md)Design least-privilege tools, validate input, and log sensitive operations for review.

## Wrap an agent in a guardrail

The most direct control is a guardrail on the model boundary. Configure one on the model provider and every prompt and response the agent handles is screened against it, with blocked content redacted from the conversation before it reaches the model again.

(( tab "Python" ))
```python
from strands import Agent
from strands.models import BedrockModel

# The guardrail screens every prompt and response; blocked content is redacted
model = BedrockModel(
    guardrail_id="your-guardrail-id",
    guardrail_version="1",
)

agent = Agent(model=model)
agent("Summarize our refund policy for a customer.")
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent, BedrockModel } from '@strands-agents/sdk'

// The guardrail screens every prompt and response; blocked content is redacted
const model = new BedrockModel({
  guardrailConfig: {
    guardrailIdentifier: 'your-guardrail-id',
    guardrailVersion: '1',
  },
})

const agent = new Agent({ model })
await agent.invoke('Summarize our refund policy for a customer.')
```
(( /tab "TypeScript" ))

For the full guardrail configuration, shadow-mode monitoring, and providers without native guardrails, see [Add guardrails](/docs/user-guide/sdk/safety-security/guardrails/index.md).

## Where to go next

Shipping an agent for the first time? Start with [guardrails](/docs/user-guide/sdk/safety-security/guardrails/index.md) to put a control on the model boundary, then [harden your prompts](/docs/user-guide/sdk/safety-security/prompt-engineering/index.md) so the system prompt holds up against adversarial input. If your agent loads history from a request body or a shared store, read [trusted message history](/docs/user-guide/sdk/safety-security/trusted-message-history/index.md) before you do.

Handling personal data or operating in a regulated environment? Add [PII redaction](/docs/user-guide/sdk/safety-security/pii-redaction/index.md) to your telemetry pipeline and follow the [responsible AI](/docs/user-guide/sdk/safety-security/responsible-ai/index.md) practices for tool design and audit logging.

## Related pages

- [Attack strategies](/docs/user-guide/evals-sdk/red-teaming/strategies/index.md) (1 shared tag)
- [Harmfulness evaluator](/docs/user-guide/evals-sdk/evaluators/harmfulness_evaluator/index.md) (1 shared tag)
- [Reading the report](/docs/user-guide/evals-sdk/red-teaming/reading_the_report/index.md) (1 shared tag)
- [Red teaming](/docs/user-guide/evals-sdk/red-teaming/index.md) (1 shared tag)
- [Refusal evaluator](/docs/user-guide/evals-sdk/evaluators/refusal_evaluator/index.md) (1 shared tag)
- [Responsible AI](/docs/user-guide/sdk/safety-security/responsible-ai/index.md) (1 shared tag)
- [Scoring attacks](/docs/user-guide/evals-sdk/red-teaming/evaluators/index.md) (1 shared tag)
- [Stereotyping evaluator](/docs/user-guide/evals-sdk/evaluators/stereotyping_evaluator/index.md) (1 shared tag)
- [Writing a custom task](/docs/user-guide/evals-sdk/red-teaming/custom_task/index.md) (1 shared tag)
- [Writing custom cases](/docs/user-guide/evals-sdk/red-teaming/custom_cases/index.md) (1 shared tag)
