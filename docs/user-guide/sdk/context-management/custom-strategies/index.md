Experimental

The Context Manager strategy API is experimental and may change in future versions.

When the [built-in modes](/docs/user-guide/sdk/context-management/built-in-modes/index.md) don’t fit, build a custom strategy pipeline. Define which content to reduce, how to reduce it, and when each strategy fires.

## Strategy pipeline

Strategies run as an ordered pipeline. Each strategy sees the output of the previous one, so order determines priority. If two strategies target the same content, the first one to shrink it below the next strategy’s threshold wins.

The SDK always appends an emergency truncation strategy as the final step. It only fires when the context window is still overflowing after all user strategies have run.

(( tab "Python" ))
```python
from strands import Agent
from strands.experimental.context_manager import Offload

agent = Agent(
    context_manager={
        "strategies": [
            Offload.truncate("tool_results").when(
                threshold=2000,
            ),
            Offload.summarize("*").when(
                utilization=0.8,
                preserve_recent=4,
            ),
        ],
    },
)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent } from '@strands-agents/sdk'
import { Offload } from '@strands-agents/sdk/experimental'

const agent = new Agent({
  contextManager: {
    strategies: [
      Offload.truncate('toolResults').when({
        threshold: 2000,
      }),
      Offload.summarize('*').when({
        utilization: 0.8,
        preserveRecent: 4,
      }),
    ],
  },
})
```
(( /tab "TypeScript" ))

Note

Both SDKs accept a config object with a `strategies``strategies` key. The SDK constructs the `ContextManager` internally.

## Offload builder

The `Offload` namespace exposes three methods. Each returns a strategy builder that can be chained with `.when()``.when()` to add conditions.

### Truncate

Replaces oversized content with a head/tail preview. The original content is stored in the stash for later retrieval.

(( tab "Python" ))
```python
from strands.experimental.context_manager import Offload

Offload.truncate(
    "tool_results",
    {"preview_tokens": 750},
).when(threshold=1500)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Offload } from '@strands-agents/sdk/experimental'

Offload.truncate('toolResults', {
  previewTokens: 750,
}).when({ threshold: 1500 })
```
(( /tab "TypeScript" ))

**Truncate configuration:**

(( tab "Python" ))
| Parameter | Key | Default |
| --- | --- | --- |
| Preview size | `preview_tokens` | 1,000 |
| Preview mode | `preview` | `"head_tail"` |
(( /tab "Python" ))

(( tab "TypeScript" ))
| Parameter | Key | Default |
| --- | --- | --- |
| Preview size | `previewTokens` | 1,000 |
| Preview mode | `preview` | `"headTail"` |
(( /tab "TypeScript" ))

Preview modes: `"head"`, `"tail"`, `"head_tail"``"headTail"`.

### Summarize

Replaces content with an LLM-generated summary. Uses `agent.aux_model``agent.auxModel` by default.

(( tab "Python" ))
```python
from strands.experimental.context_manager import Offload

Offload.summarize("*").when(
    utilization=0.85,
    preserve_recent=4,
)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Offload } from '@strands-agents/sdk/experimental'

Offload.summarize('*').when({
  utilization: 0.85,
  preserveRecent: 4,
})
```
(( /tab "TypeScript" ))

**Summarize configuration:**

(( tab "Python" ))
| Parameter | Key | Default |
| --- | --- | --- |
| Model | `model` | `agent.aux_model` |
| System prompt | `system_prompt` | Built-in |
(( /tab "Python" ))

(( tab "TypeScript" ))
| Parameter | Key | Default |
| --- | --- | --- |
| Model | `model` | `agent.auxModel` |
| System prompt | `systemPrompt` | Built-in |
(( /tab "TypeScript" ))

### Drop

Removes matching content entirely. No preview, no stash entry.

(( tab "Python" ))
```python
from strands.experimental.context_manager import Offload

Offload.drop("tool_results").when(preserve_recent=5)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Offload } from '@strands-agents/sdk/experimental'

Offload.drop('toolResults').when({
  preserveRecent: 5,
})
```
(( /tab "TypeScript" ))

## Conditions

Chain `.when()``.when()` to control when a strategy fires. Conditions determine the granularity of the strategy, not the method.

| Condition | Granularity | Behavior |
| --- | --- | --- |
| `threshold``threshold` only | Per-block, eager | Acts on each block above this token size on message arrival |
| `utilization``utilization` only | Message-level, batch | Removes/summarizes oldest messages when utilization exceeded |
| Both | Message-level | Targets messages with blocks over the threshold, fires at utilization |
| `preserve_recent``preserveRecent` | — | Number of most recent matching messages to skip |

`preserve_recent``preserveRecent` accepts an integer (absolute count) or a float between 0 and 1 (ratio of matching messages, e.g., `0.7` keeps 70%).

### Per-block example

Fire eagerly on individual blocks over 2,000 tokens:

(( tab "Python" ))
```python
from strands.experimental.context_manager import Offload

Offload.truncate("tool_results").when(threshold=2000)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Offload } from '@strands-agents/sdk/experimental'

Offload.truncate('toolResults').when({
  threshold: 2000,
})
```
(( /tab "TypeScript" ))

### Message-level example

Summarize oldest messages when the window reaches 85%:

(( tab "Python" ))
```python
from strands.experimental.context_manager import Offload

Offload.summarize("*").when(
    utilization=0.85,
    preserve_recent=4,
)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Offload } from '@strands-agents/sdk/experimental'

Offload.summarize('*').when({
  utilization: 0.85,
  preserveRecent: 4,
})
```
(( /tab "TypeScript" ))

### Combined example

Target tool results over 1,500 tokens, but only fire when the window reaches 90%:

(( tab "Python" ))
```python
from strands.experimental.context_manager import Offload

Offload.truncate("tool_results").when(
    threshold=1500,
    utilization=0.9,
)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Offload } from '@strands-agents/sdk/experimental'

Offload.truncate('toolResults').when({
  threshold: 1500,
  utilization: 0.9,
})
```
(( /tab "TypeScript" ))

## Targets

Targets specify which content a strategy applies to.

(( tab "Python" ))
| Target | Value |
| --- | --- |
| All content | `"*"` |
| Tool results | `"tool_results"` |
| Failed tool results | `"tool_result_errors"` |
| Assistant text | `"assistant_text"` |
| User text | `"user_text"` |
| Specific tools | `["tool::bash", "tool::read_file"]` |
| Exclude tools | `["!tool::bash"]` |
(( /tab "Python" ))

(( tab "TypeScript" ))
| Target | Value |
| --- | --- |
| All content | `"*"` |
| Tool results | `"toolResults"` |
| Failed tool results | `"toolResultErrors"` |
| Assistant text | `"assistantText"` |
| User text | `"userText"` |
| Specific tools | `["tool::bash", "tool::readFile"]` |
| Exclude tools | `["!tool::bash"]` |
(( /tab "TypeScript" ))

Tool name lists use the `tool::` prefix. Prefix a name with `!` to exclude it (apply to all tools *except* the listed ones).

## Stash

The stash stores all message content on arrival as JSON, before any strategy runs. Truncated or summarized content can be retrieved on demand through the `retrieve_context` tool, which the SDK registers by default.

Stash uses in-memory storage by default. Configure it through the `stash``stash` key:

-   Omit or pass `true` for defaults (in-memory storage)
-   Pass a config with a custom storage backend
-   Pass `false` to disable stash entirely

(( tab "Python" ))
```python
from strands import Agent

# Disable stash and retrieval tool
agent = Agent(
    context_manager={
        "stash": False,
    },
)
```
(( /tab "Python" ))

(( tab "TypeScript" ))
```typescript
import { Agent } from '@strands-agents/sdk'

const agent = new Agent({
  contextManager: {
    stash: false,
  },
})
```
(( /tab "TypeScript" ))

## Emergency truncation

Every strategy pipeline ends with an emergency truncation strategy, appended automatically. It fires only when the context window is still overflowing after all user strategies have run. When it fires, it drops the oldest 20% of non-head messages.

Emergency truncation intentionally ignores pinned messages so an all-pinned overflow is still recoverable. Regular strategies respect pins.

## Related pages

- [Built-in Modes](/docs/user-guide/sdk/context-management/built-in-modes/index.md) (2 shared tags)
- [Context Estimation](/docs/user-guide/sdk/context-management/context-estimation/index.md) (2 shared tags)
- [Context management](/docs/user-guide/sdk/context-management/index.md) (2 shared tags)
- [Strategy Presets](/docs/user-guide/sdk/context-management/presets/index.md) (2 shared tags)
- [Context Offloader](/docs/user-guide/sdk/plugins/context-offloader/index.md) (2 shared tags)
- [Conversation Management](/docs/user-guide/sdk/agents/conversation-management/index.md) (2 shared tags)
- [Context Injector](/docs/user-guide/sdk/plugins/context-injector/index.md) (1 shared tag)
- [Coherence evaluator](/docs/user-guide/evals-sdk/evaluators/coherence_evaluator/index.md) (1 shared tag)
- [Conciseness evaluator](/docs/user-guide/evals-sdk/evaluators/conciseness_evaluator/index.md) (1 shared tag)
- [Goal success rate evaluator](/docs/user-guide/evals-sdk/evaluators/goal_success_rate_evaluator/index.md) (1 shared tag)


## Implementation

### Python

- [harness-sdk/strands-py/src/strands/_context_manager/strategies/offload/base.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/_context_manager/strategies/offload/base.py)
- [harness-sdk/strands-py/src/strands/_context_manager/strategies/offload/truncate.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/_context_manager/strategies/offload/truncate.py)
- [harness-sdk/strands-py/src/strands/_context_manager/strategies/offload/summarize.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/_context_manager/strategies/offload/summarize.py)

### TypeScript

- [harness-sdk/strands-ts/src/context-manager/strategies/offload/base.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/strategies/offload/base.ts)
- [harness-sdk/strands-ts/src/context-manager/strategies/offload/index.ts](https://github.com/strands-agents/harness-sdk/blob/main/strands-ts/src/context-manager/strategies/offload/index.ts)
