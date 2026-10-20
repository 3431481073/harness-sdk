A prompt against a single agent instance can, left unbounded, loop longer than you want, spend more tokens than you budgeted, or keep running after the caller has walked away. When you run agents in production, you need to cap that work, stop it on demand, and read back a clear reason for why it ended.

This page collects the controls the [agent loop](/docs/user-guide/sdk/agents/agent-loop/index.md) exposes for exactly that: bounding a single call, cancelling one mid-flight, interpreting the stop reason it returns, recovering from tool and model errors, and running one agent safely across many concurrent requests. Each control works on its own; the [worked example](#worked-example-a-high-concurrency-service) at the end combines them into one request handler.

## Cap the work one call can do

To bound a single invocation, pass a set of limits alongside the prompt. You can cap the number of turns (loop iterations), the output tokens, or the total tokens. All three are optional, and each must be a positive integer.

(( tab "Python" ))
```python
from strands import Agent

agent = Agent()

result = agent(
    "Summarize this document",
    limits={
        "turns": 5,
        "output_tokens": 2000,
        "total_tokens": 10000,
    },
)

if result.stop_reason == "limit_turns":
    print("Hit turn budget")
elif result.stop_reason == "limit_total_tokens":
    print("Hit token budget")
```

The same parameter works with `invoke_async` and `stream_async`.
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent } from '@strands-agents/sdk'

const agent = new Agent()

const result = await agent.invoke('Summarize this document', {
  limits: {
    turns: 5,
    outputTokens: 2000,
    totalTokens: 10000,
  },
})

if (result.stopReason === 'limitTurns') {
  console.log('Hit turn budget')
} else if (result.stopReason === 'limitTotalTokens') {
  console.log('Hit token budget')
}
```

The same option works with `stream`. Each cap must be a positive finite number.
(( /tab "TypeScript" ))

Limits are checked at the top of each loop iteration, not mid-call. A single turn can overshoot its token budget, but the check fires before the next turn starts, and tools requested by the previous turn always finish first. When several caps trip at once, the reported stop reason follows priority order: turns, then total tokens, then output tokens.

Limits apply to the current invocation only. A reused agent starts each call with fresh counters, and the message history stays in a valid, reinvokable state, so you can retry with a higher budget.

## Know why the loop stopped

Every result carries a stop reason that tells you whether the call finished, hit a budget, was cancelled, or was blocked. Branch on it to decide what happens next. Read it from `result.stop_reason``result.stopReason`.

| Stop reason | What it means | What to do |
| --- | --- | --- |
| `end_turn``endTurn` | Normal completion. The model finished its response. | Return the result. |
| `stop_sequence``stopSequence` | The model hit a configured stop sequence. | Terminates normally, like `end_turn`. |
| `tool_use``toolUse` | The model requested a tool. The loop handles this internally. | Nothing; you see this only mid-loop. |
| `limit_turns``limitTurns` | The turn budget was exhausted. | Reinvoke with a higher budget, or return a partial answer. |
| `limit_total_tokens``limitTotalTokens` | The cumulative token budget was exhausted. | Same as above; history is reinvokable. |
| `limit_output_tokens``limitOutputTokens` | The output token budget was exhausted. | Same as above. |
| `cancelled` | The agent was stopped via `agent.cancel()``agent.cancel()` or a cancel signal. | Treat as a client-initiated stop. |
| `max_tokens``maxTokens` | A single model response exceeded the provider’s per-call cap. Unrecoverable within the loop. | See [Handle a truncated model response](#handle-a-truncated-model-response). |
| `content_filtered``contentFiltered` | A safety mechanism blocked the response. | Handle per your application’s policy. |
| `guardrail_intervened``guardrailIntervened` | A guardrail policy stopped generation. | Handle per your application’s policy. |
| `interrupt` | The agent paused for human input. | Resume with interrupt responses. See [Interrupts](/docs/user-guide/sdk/interrupts/index.md). |

The three limit reasons signal graceful budget exhaustion, not failure. Content filtering and guardrail intervention both terminate the loop and should be handled deliberately rather than retried blindly.

## Stop a running agent

To stop a call from outside the loop, on a client disconnect, a timeout, or a “Stop” button, cancel it. The agent checks for cancellation at fixed checkpoints and returns a result with a `cancelled` stop reason. The cancel signal clears when the invocation completes, so the agent is immediately reusable. `agent.cancel()``agent.cancel()` is idempotent; calling it more than once is safe.

(( tab "Python" ))
```python
import threading
import time

from strands import Agent


def timeout_watchdog(agent: Agent, timeout: float) -> None:
    """Cancel the agent after a timeout period."""
    time.sleep(timeout)
    agent.cancel()


agent = Agent()

watchdog = threading.Thread(target=timeout_watchdog, args=(agent, 30.0))
watchdog.start()

result = agent("Analyze this large dataset")
watchdog.join()

if result.stop_reason == "cancelled":
    print("Agent was cancelled due to timeout")
```

`cancel()` is thread-safe. For a declarative deadline, pass your own `threading.Event` as the `cancel_signal` parameter to `__call__`, `invoke_async`, or `stream_async`. The agent watches both its internal signal and your event, and never sets or clears the event itself.

```python
import threading

from strands import Agent

agent = Agent()

cancel_signal = threading.Event()
threading.Timer(30.0, cancel_signal.set).start()

result = agent("Analyze this large dataset", cancel_signal=cancel_signal)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent } from '@strands-agents/sdk'

const agent = new Agent()

// Cancel from a timer after 30 seconds
setTimeout(() => agent.cancel(), 30_000)

const result = await agent.invoke('Analyze this large dataset')

if (result.stopReason === 'cancelled') {
  console.log('Agent was cancelled due to timeout')
}
```

For a declarative deadline, pass an `AbortSignal` as the `cancelSignal` option to `invoke` or `stream`. The agent composes it with its internal controller, so `agent.cancel()` and the external signal each trigger cancellation independently.

```typescript
import { Agent } from '@strands-agents/sdk'

const agent = new Agent()

// Cancel the invocation if it runs past a 20-second deadline
const result = await agent.invoke('Analyze this large dataset', {
  cancelSignal: AbortSignal.timeout(20_000),
})

if (result.stopReason === 'cancelled') {
  console.log('Agent hit its deadline')
}
```
(( /tab "TypeScript" ))

The agent checks for cancellation before and between tool calls, so a running tool is not interrupted on its own. Once a tool starts, cancellation is cooperative: the tool decides whether to stop early. Long-running tools should poll the cancel signal between steps, or forward it to any API that accepts one.

(( tab "Python" ))
```python
from strands import tool
from strands.types.tools import ToolContext


@tool(context=True)
def long_job(tool_context: ToolContext) -> str:
    """Do chunked work, checking for cancellation between chunks."""
    for chunk in chunks:
        if tool_context.cancel_signal.is_set():
            return "cancelled"
        process(chunk)
    return "done"
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { tool } from '@strands-agents/sdk'
import { z } from 'zod'

const fetchResource = tool({
  name: 'fetch_resource',
  description: 'Fetch a large resource, respecting cancellation',
  inputSchema: z.object({ url: z.string() }),
  callback: async (input, context) => {
    // Forward the signal so the request aborts when the agent is cancelled
    const response = await fetch(input.url, { signal: context?.cancelSignal })
    return response.text()
  },
})
```
(( /tab "TypeScript" ))

For the full checkpoint tables and provider-level abort behavior, see [Cancellation](/docs/user-guide/sdk/agents/agent-loop/index.md#cancellation) in the agent loop reference. Cancellation stops the agent entirely; it differs from an [interrupt](/docs/user-guide/sdk/interrupts/index.md), which pauses for human input and can resume.

## Recover from tool and model errors

A tool that fails does not crash the loop. The execution system captures the error, returns it to the model as an error result, and lets the model adjust or try an alternative. That default recovery covers most cases. Two mechanisms give you more control:

-   **Model provider errors** such as rate limits retry automatically with exponential backoff. To change the attempt count, backoff, or which errors are retryable, configure a strategy. See [Retry Strategies](/docs/user-guide/sdk/agents/retry-strategies/index.md).
-   **Tool-level recovery** such as retrying a flaky tool, propagating an unexpected exception instead of feeding it back to the model, or capping how often a tool runs is done with [Hooks](/docs/user-guide/sdk/agents/hooks/index.md). The hooks cookbook covers [model call retry](/docs/user-guide/sdk/agents/hooks/index.md#model-call-retry), [tool call retry](/docs/user-guide/sdk/agents/hooks/index.md#tool-call-retry), and [exception handling](/docs/user-guide/sdk/agents/hooks/index.md#exception-handling).

### Handle a truncated model response

When a single model response exceeds the provider’s per-call output cap, the loop cannot continue from a partial message. This is distinct from the graceful `limit_*` stop reasons: the loop raises `MaxTokensReachedException``MaxTokensError` rather than returning a result. Reduce the context size, raise the provider’s token limit, or split the task into smaller steps.

## Run one agent across many requests

An agent mutates its conversation history as each invocation runs, so overlapping calls on one instance would interleave their messages and corrupt the history. By default the agent processes one invocation at a time and rejects overlap.

(( tab "Python" ))
Invoking an agent that is already running raises `ConcurrencyException`. The `concurrent_invocation_mode` constructor parameter controls this: it takes a `ConcurrentInvocationMode` of either `THROW` (the default) or `UNSAFE_REENTRANT`.

```python
from strands import Agent
from strands.types.exceptions import ConcurrencyException

agent = Agent()

try:
    result = agent("Summarize this report")
except ConcurrencyException:
    # Another invocation is already running on this agent instance
    ...
```

When a retry arrives for a request that is still in flight, deduplicate it rather than erroring or doing the work twice. Pass `idempotency_token` to any invocation method to identify the logical request. A second call with the same token waits for the original and returns the same `AgentResult`; a call with a different token still raises `ConcurrencyException`.

```python
result = agent("Process order 1234", idempotency_token="order-1234")
```

`UNSAFE_REENTRANT` removes the single-invocation guard entirely, and nothing then protects the history from concurrent mutation. To run independent work in parallel, a separate agent per task is safer than sharing one.
(( /tab "Python" ))

(( tab "TypeScript" ))
Invoking an agent that is already running throws `ConcurrentInvocationError`. This SDK does not offer a configurable concurrency mode or idempotency-token deduplication of retries; both are available only in the Python SDK. To run independent work in parallel, use a separate agent per task.
(( /tab "TypeScript" ))

## Worked example: a high-concurrency service

A service that fields thousands of concurrent invocations puts every control above to work at once. The pattern that scales is one fresh agent per request: it sidesteps the concurrency guard entirely, since no two requests share an instance. Each request gets a bounded turn count, a per-run token budget, and a deadline, and the handler maps the stop reason onto a typed outcome the caller can branch on.

(( tab "Python" ))
```python
import threading
from dataclasses import dataclass
from enum import Enum

from strands import Agent
from strands.models import BedrockModel

MODEL_ID = "global.anthropic.claude-sonnet-5"


class Outcome(str, Enum):
    COMPLETED = "completed"
    BUDGET_EXCEEDED = "budget_exceeded"
    TIMED_OUT = "timed_out"


@dataclass
class Reply:
    outcome: Outcome
    text: str


def classify(stop_reason: str) -> Outcome:
    if stop_reason == "cancelled":
        return Outcome.TIMED_OUT
    if stop_reason in ("limit_turns", "limit_total_tokens", "limit_output_tokens"):
        return Outcome.BUDGET_EXCEEDED
    return Outcome.COMPLETED


def handle_request(prompt: str, deadline_seconds: float = 20.0) -> Reply:
    """Run one request on its own agent with bounded turns, tokens, and time."""
    # A fresh agent per request keeps concurrent calls from sharing history
    agent = Agent(model=BedrockModel(model_id=MODEL_ID))

    cancel_signal = threading.Event()
    threading.Timer(deadline_seconds, cancel_signal.set).start()

    result = agent(
        prompt,
        limits={"turns": 6, "total_tokens": 20_000},
        cancel_signal=cancel_signal,
    )

    return Reply(outcome=classify(result.stop_reason), text=str(result))
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent, BedrockModel } from '@strands-agents/sdk'

const MODEL_ID = 'global.anthropic.claude-sonnet-5'

type Outcome = 'completed' | 'budgetExceeded' | 'timedOut'

function classify(stopReason: string): Outcome {
  if (stopReason === 'cancelled') return 'timedOut'
  if (
    stopReason === 'limitTurns' ||
    stopReason === 'limitTotalTokens' ||
    stopReason === 'limitOutputTokens'
  ) {
    return 'budgetExceeded'
  }
  return 'completed'
}

async function handleRequest(prompt: string, deadlineMs = 20_000) {
  // A fresh agent per request keeps concurrent calls from sharing history
  const agent = new Agent({ model: new BedrockModel({ modelId: MODEL_ID }) })

  const result = await agent.invoke(prompt, {
    limits: { turns: 6, totalTokens: 20_000 },
    cancelSignal: AbortSignal.timeout(deadlineMs),
  })

  return { outcome: classify(result.stopReason), message: result.lastMessage }
}
```
(( /tab "TypeScript" ))

The handler never raises on a budget or a deadline: those come back as a `BUDGET_EXCEEDED` or `TIMED_OUT` outcome with the partial work intact, so the caller decides whether to retry, return a partial answer, or fail. Only a genuine error, such as a truncated model response, propagates as an exception.

## Related pages

- [Retry Strategies](/docs/user-guide/sdk/agents/retry-strategies/index.md) (2 shared tags)
- [Interrupts](/docs/user-guide/sdk/interrupts/index.md) (2 shared tags)
- [Model Routing](/docs/user-guide/sdk/model-providers/model-routing/index.md) (1 shared tag)
- [Interrupts in Multi-Agent Systems](/docs/user-guide/sdk/interrupts-multi-agent/index.md) (2 shared tags)
- [Middleware](/docs/user-guide/sdk/agents/middleware/index.md) (1 shared tag)
- [Tool Executors](/docs/user-guide/sdk/tools/executors/index.md) (1 shared tag)
- [Build a custom plugin](/docs/user-guide/sdk/plugins/custom-plugins/index.md) (1 shared tag)
- [Plugins](/docs/user-guide/sdk/plugins/index.md) (1 shared tag)
- [Chaos testing](/docs/user-guide/evals-sdk/chaos_testing/index.md) (1 shared tag)
- [Structured output](/docs/user-guide/sdk/agents/structured-output-behavior/index.md) (1 shared tag)


## Implementation

### Python

- [harness-sdk/strands-py/src/strands/agent/agent.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/agent/agent.py)
- [harness-sdk/strands-py/src/strands/types/event_loop.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/event_loop.py)

### TypeScript

- [harness-sdk/strands-ts/src/agent/agent.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/agent/agent.ts)
- [harness-sdk/strands-ts/src/types/messages.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/types/messages.ts)
