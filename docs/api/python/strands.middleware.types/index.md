Middleware type system.

## MiddlewareInputPhase

```python
class MiddlewareInputPhase(Generic[TContext, TResult, TEvent])
```

Defined in: [src/strands/middleware/types.py:13](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/types.py#L13)

Phase sub-token for Input handlers — transforms context before execution.

#### \_\_init\_\_

```python
def __init__(stage: MiddlewareStage[TContext, TResult, TEvent]) -> None
```

Defined in: [src/strands/middleware/types.py:18](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/types.py#L18)

Bind this phase sub-token to its parent stage.

## MiddlewareWrapPhase

```python
class MiddlewareWrapPhase(Generic[TContext, TResult, TEvent])
```

Defined in: [src/strands/middleware/types.py:24](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/types.py#L24)

Phase sub-token for Wrap handlers — full async generator wrap.

#### \_\_init\_\_

```python
def __init__(stage: MiddlewareStage[TContext, TResult, TEvent]) -> None
```

Defined in: [src/strands/middleware/types.py:29](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/types.py#L29)

Bind this phase sub-token to its parent stage.

## MiddlewareOutputPhase

```python
class MiddlewareOutputPhase(Generic[TContext, TResult, TEvent])
```

Defined in: [src/strands/middleware/types.py:35](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/types.py#L35)

Phase sub-token for Output handlers — transforms result after execution.

#### \_\_init\_\_

```python
def __init__(stage: MiddlewareStage[TContext, TResult, TEvent]) -> None
```

Defined in: [src/strands/middleware/types.py:40](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/types.py#L40)

Bind this phase sub-token to its parent stage.

## MiddlewareStage

```python
class MiddlewareStage(Generic[TContext, TResult, TEvent])
```

Defined in: [src/strands/middleware/types.py:46](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/types.py#L46)

A stage token identifying a middleware interception point.

Only the SDK’s built-in tokens (`InvokeModelStage`, `ExecuteToolStage`) are invoked; constructing a custom stage is unsupported.

**Attributes**:

-   `name` - Human-readable name for debugging and logging.
-   `result_type` - The wrapper class Output handlers receive and return (`TResult`).
-   `result_event` - The event class that is this stage’s result; the registry and the call sites select it from the stream by type, so Wrap handlers may yield other events before or after it.

#### \_\_init\_\_

```python
def __init__(name: str, *, result_type: type[TResult],
             result_event: type[Any]) -> None
```

Defined in: [src/strands/middleware/types.py:62](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/types.py#L62)

Create a stage token with its Input/Wrap/Output phase sub-tokens.

#### \_\_repr\_\_

```python
def __repr__() -> str
```

Defined in: [src/strands/middleware/types.py:71](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/types.py#L71)

Return a debug representation naming the stage.

#### \_\_hash\_\_

```python
def __hash__() -> int
```

Defined in: [src/strands/middleware/types.py:75](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/types.py#L75)

Hash by identity so each stage token is a distinct registry key.

#### \_\_eq\_\_

```python
def __eq__(other: object) -> bool
```

Defined in: [src/strands/middleware/types.py:79](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/middleware/types.py#L79)

Compare by identity — a stage token equals only itself.