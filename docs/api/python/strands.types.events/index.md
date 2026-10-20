Public stream event types.

The agent stream is a sequence of `TypedEvent` instances. The types in this module are public because middleware constructs or receives them: `ModelStopReason` is the result of a model call and `ToolResultEvent` is the result of a tool call. The other stream events are internal.

## TypedEvent

```python
class TypedEvent(dict)
```

Defined in: [src/strands/types/events.py:19](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L19)

Base class for every event in the agent stream.

An event is a dict whose items are its payload. Events that a middleware Wrap handler yields into the stream must be `TypedEvent` instances: the agent loop calls `prepare()` and reads `is_callback_event` on every event, so a plain dict fails.

#### \_\_init\_\_

```python
def __init__(data: dict[str, Any] | None = None) -> None
```

Defined in: [src/strands/types/events.py:27](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L27)

Initialize the typed event with optional data.

**Arguments**:

-   `data` - Optional dictionary of event data to initialize with

#### is\_callback\_event

```python
@property
def is_callback_event() -> bool
```

Defined in: [src/strands/types/events.py:36](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L36)

True if this event should trigger the callback\_handler to fire.

#### as\_dict

```python
def as_dict() -> dict
```

Defined in: [src/strands/types/events.py:40](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L40)

Convert this event to a raw dictionary for emitting purposes.

#### prepare

```python
def prepare(invocation_state: dict) -> None
```

Defined in: [src/strands/types/events.py:44](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L44)

Prepare the event for emission by adding invocation state.

This allows a subset of events to merge with the invocation\_state without needing to pass around the invocation\_state throughout the system.

## ModelStopReason

```python
class ModelStopReason(TypedEvent)
```

Defined in: [src/strands/types/events.py:53](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L53)

Final event of a model call, carrying the aggregated response.

This is the result event of `InvokeModelStage`: the model stream ends with it, an Output handler receives it as `InvokeModelResult.result`, and a Wrap handler yields one to short-circuit the model call. Read it through `stop_reason`, `message`, `usage` and `metrics`. `event["stop"]` holds the same values as a `(stop_reason, message, usage, metrics)` tuple for model providers that unpack it from `process_stream`. It is not sent to callback handlers.

#### \_\_init\_\_

```python
def __init__(stop_reason: StopReason, message: Message, usage: Usage,
             metrics: Metrics) -> None
```

Defined in: [src/strands/types/events.py:64](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L64)

Initialize with the final execution results.

**Arguments**:

-   `stop_reason` - Why the model stopped generating
-   `message` - Final message from the model
-   `usage` - Usage information from the model
-   `metrics` - Execution metrics and performance data

#### stop\_reason

```python
@property
def stop_reason() -> StopReason
```

Defined in: [src/strands/types/events.py:86](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L86)

Why the model stopped generating.

#### message

```python
@property
def message() -> Message
```

Defined in: [src/strands/types/events.py:91](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L91)

Final message from the model.

#### usage

```python
@property
def usage() -> Usage
```

Defined in: [src/strands/types/events.py:96](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L96)

Usage information from the model.

#### metrics

```python
@property
def metrics() -> Metrics
```

Defined in: [src/strands/types/events.py:101](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L101)

Execution metrics and performance data.

## ToolResultEvent

```python
class ToolResultEvent(TypedEvent)
```

Defined in: [src/strands/types/events.py:111](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L111)

Final event of a tool call, carrying the tool result.

This is the result event of `ExecuteToolStage`: tool execution ends with it, an Output handler receives it as `ExecuteToolResult.result`, and a Wrap handler yields one to short-circuit or deny the tool call. When building a replacement for an existing result, pass its `exception` through so `AfterToolCallEvent` still receives it. It is not sent to callback handlers.

#### \_\_init\_\_

```python
def __init__(tool_result: ToolResult,
             exception: Exception | None = None,
             *,
             backgrounded: bool = False) -> None
```

Defined in: [src/strands/types/events.py:120](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L120)

Initialize tool result event.

**Arguments**:

-   `tool_result` - The tool result returned to the model.
-   `exception` - The exception behind an error result, if any.
-   `backgrounded` - Whether this result only acknowledges that the tool was dispatched to the background.

#### backgrounded

```python
@property
def backgrounded() -> bool
```

Defined in: [src/strands/types/events.py:136](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L136)

Whether this result only acknowledges that the tool was dispatched to the background.

#### exception

```python
@property
def exception() -> Exception | None
```

Defined in: [src/strands/types/events.py:141](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L141)

The original exception that occurred, if any.

Can be used for re-raising or type-based error handling.

#### tool\_use\_id

```python
@property
def tool_use_id() -> str
```

Defined in: [src/strands/types/events.py:149](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L149)

The toolUseId associated with this result.

#### tool\_result

```python
@property
def tool_result() -> ToolResult
```

Defined in: [src/strands/types/events.py:154](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/types/events.py#L154)

Final result from the completed tool execution.