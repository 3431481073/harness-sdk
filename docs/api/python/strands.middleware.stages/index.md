Built-in middleware stages and their context/result types.

## InvokeModelContext

```python
@dataclass
class InvokeModelContext()
```

Defined in: [src/strands/middleware/stages.py:39](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/stages.py#L39)

Context passed to InvokeModelStage middleware.

The collection fields (messages, system\_prompt, tool\_specs, tool\_choice) are defensive copies, so middleware cannot accidentally mutate agent state. `invocation_state` and `model` are instead shared by reference: `invocation_state` is the live dict hooks and tools write to during streaming, and `model` is the model this call invokes (it starts as `agent.model`; middleware may replace it per call).

#### invocation\_context

The request this model call belongs to, if any; shared by reference.

#### replace

```python
def replace(*,
            messages: Messages = _UNSET,
            system_prompt: SystemPrompt = _UNSET,
            tool_specs: list[ToolSpec] = _UNSET,
            tool_choice: ToolChoice | None = _UNSET,
            invocation_state: dict[str, Any] = _UNSET,
            model: Model = _UNSET,
            projected_input_tokens: int | None = _UNSET,
            dynamic_trailing_blocks: int = _UNSET) -> InvokeModelContext
```

Defined in: [src/strands/middleware/stages.py:62](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/stages.py#L62)

Return a copy with the given fields replaced; omitted fields keep their current value.

**Example**:

```python
modified = context.replace(system_prompt="Be concise.")
```

**Arguments**:

-   `messages` - Messages to send to the model.
-   `system_prompt` - System prompt guiding the model.
-   `tool_specs` - Tool specifications available to the model.
-   `tool_choice` - How the model selects tools.
-   `invocation_state` - Per-invocation state, shared by reference across the run.
-   `model` - The model this call invokes.
-   `projected_input_tokens` - Estimated input token count for this call.
-   `dynamic_trailing_blocks` - Trailing blocks of the last user message rebuilt each call.

**Returns**:

A new `InvokeModelContext`.

## InvokeModelResult

```python
@dataclass
class InvokeModelResult()
```

Defined in: [src/strands/middleware/stages.py:108](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/stages.py#L108)

Result passed to and returned from `InvokeModelStage.Output` handlers.

**Attributes**:

-   `result` - The `ModelStopReason` event that ends the model call.

#### InvokeModelStage

Built-in stage wrapping core model invocation.

Middleware registered for this stage can rate-limit, cache, or transform model inputs/outputs.

## MiddlewareInterruptResult

```python
@dataclass
class MiddlewareInterruptResult()
```

Defined in: [src/strands/middleware/stages.py:128](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/stages.py#L128)

Value returned by a middleware `interrupt()` when the agent resumes.

Wrapping the response (rather than returning it bare) mirrors the TypeScript SDK and leaves room to add fields later without breaking callers.

**Attributes**:

-   `response` - The human-provided response the agent resumed with.

## ExecuteToolContext

```python
@dataclass
class ExecuteToolContext()
```

Defined in: [src/strands/middleware/stages.py:181](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/stages.py#L181)

Context passed to ExecuteToolStage middleware.

`tool_use` is a shallow copy of the executor’s dict, so reassigning its top-level keys cannot corrupt executor state. Its `input` value is shared by reference (it can hold non-copyable objects, such as the agent injected on direct tool calls), so mutating `input` in place still leaks; build a new `tool_use` and pass it through `replace()` instead. `invocation_state` is shared by reference, as hooks receive it.

`cancel_signal` is executor-owned: middleware can observe it, but the tool always receives the executor’s signal, not the one on this context.

Supports middleware-initiated interrupts via `interrupt()` for human-in-the-loop approval flows.

#### invocation\_context

The request this tool call belongs to, if any; the tool receives it on its `ToolContext`.

#### interrupt

```python
def interrupt(name: str,
              *,
              reason: Any = None,
              response: Any = None) -> MiddlewareInterruptResult
```

Defined in: [src/strands/middleware/stages.py:207](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/stages.py#L207)

Request a human-in-the-loop interrupt.

On first execution (no prior response) this raises `InterruptException` to halt the agent. After the user resumes with a response, the second call returns that response. Providing `response` preemptively skips the interrupt entirely.

This method is read-only with respect to interrupt state: it inspects prior responses but does not register the interrupt itself. The tool executor registers it (in its `InterruptException` handler) as the single source of truth, matching the TypeScript SDK where middleware interrupts never write to interrupt state.

**Arguments**:

-   `name` - User-defined name for the interrupt. The interrupt id is scoped to the tool call (`v1:middleware_execute_tool:<toolUseId>:<uuid5(name)>`) but not to the individual middleware, so the name must be unique across all middleware that interrupt this tool call — two middleware using the same name on the same tool call collide and share one response. (This matches the hook/tool interrupt contract, which is likewise unique per tool call, not per callback.)
-   `reason` - Optional reason for the interrupt (surfaced to the user).
-   `response` - Optional preemptive response — when set, no interrupt is raised.

**Returns**:

The user’s response wrapped in a `MiddlewareInterruptResult`.

**Raises**:

-   `InterruptException` - When no response is available yet and none was provided.

#### replace

```python
def replace(*,
            tool: AgentTool | None = _UNSET,
            tool_use: ToolUse = _UNSET,
            invocation_state: dict[str, Any] = _UNSET) -> ExecuteToolContext
```

Defined in: [src/strands/middleware/stages.py:247](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/stages.py#L247)

Return a copy with the given fields replaced; omitted fields keep their current value.

`agent`, `cancel_signal`, and the interrupt state are carried over unchanged.

**Example**:

```python
modified = context.replace(tool_use=\{**context.tool_use, "input": cleaned})
```

**Arguments**:

-   `tool` - The resolved tool implementation, or `None` if not found.
-   `tool_use` - The tool use request (name, toolUseId, input).
-   `invocation_state` - Per-invocation state, shared by reference across the run.

**Returns**:

A new `ExecuteToolContext`.

## ExecuteToolResult

```python
@dataclass
class ExecuteToolResult()
```

Defined in: [src/strands/middleware/stages.py:275](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/stages.py#L275)

Result passed to and returned from `ExecuteToolStage.Output` handlers.

**Attributes**:

-   `result` - The `ToolResultEvent` produced by the tool call.

#### ExecuteToolStage

Built-in stage wrapping individual tool execution.

Middleware registered for this stage can add telemetry, validate inputs, mock responses, or gate execution behind a human-in-the-loop interrupt.