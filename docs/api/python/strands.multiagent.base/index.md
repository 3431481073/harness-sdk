Multi-Agent Base Class.

Provides minimal foundation for multi-agent patterns (Swarm, Graph).

## Status

```python
class Status(Enum)
```

Defined in: [src/strands/multiagent/base.py:26](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L26)

Execution status for both graphs and nodes.

**Attributes**:

-   `PENDING` - Task has not started execution yet.
-   `DISPATCHED` - Node has been dispatched but execution has not started yet.
-   `EXECUTING` - Task is currently running.
-   `COMPLETED` - Task finished successfully.
-   `FAILED` - Task encountered an error and could not complete.
-   `INTERRUPTED` - Task was interrupted by user.

## NodeResult

```python
@dataclass
class NodeResult()
```

Defined in: [src/strands/multiagent/base.py:47](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L47)

Unified result from node execution - handles both Agent and nested MultiAgentBase results.

#### \_\_str\_\_

```python
def __str__() -> str
```

Defined in: [src/strands/multiagent/base.py:63](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L63)

Return a human-readable string representation of the node result.

Delegates to the inner result’s string representation:

-   AgentResult: Uses AgentResult.**str** (extracts text content)
-   MultiAgentResult: Uses MultiAgentResult.**str** (recursive)
-   Exception: Uses the exception’s string representation

**Returns**:

String representation of the node’s result.

#### get\_agent\_results

```python
def get_agent_results() -> list[AgentResult]
```

Defined in: [src/strands/multiagent/base.py:76](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L76)

Get all AgentResult objects from this node, flattened if nested.

#### to\_dict

```python
def to_dict() -> dict[str, Any]
```

Defined in: [src/strands/multiagent/base.py:89](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L89)

Convert NodeResult to JSON-serializable dict, ignoring state field.

#### from\_dict

```python
@classmethod
def from_dict(cls, data: dict[str, Any]) -> "NodeResult"
```

Defined in: [src/strands/multiagent/base.py:110](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L110)

Rehydrate a NodeResult from persisted JSON.

## MultiAgentResult

```python
@dataclass
class MultiAgentResult()
```

Defined in: [src/strands/multiagent/base.py:145](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L145)

Result from multi-agent execution with accumulated metrics.

#### \_\_str\_\_

```python
def __str__() -> str
```

Defined in: [src/strands/multiagent/base.py:156](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L156)

Return a human-readable string representation of the multi-agent result.

Priority order:

1.  Interrupts (if present) → stringified list of interrupt dicts
2.  Node results → each node’s string output, prefixed with node name

**Returns**:

String representation based on the priority order above.

#### from\_dict

```python
@classmethod
def from_dict(cls, data: dict[str, Any]) -> "MultiAgentResult"
```

Defined in: [src/strands/multiagent/base.py:181](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L181)

Rehydrate a MultiAgentResult from persisted JSON.

#### to\_dict

```python
def to_dict() -> dict[str, Any]
```

Defined in: [src/strands/multiagent/base.py:205](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L205)

Convert MultiAgentResult to JSON-serializable dict.

## MultiAgentBase

```python
class MultiAgentBase(ABC)
```

Defined in: [src/strands/multiagent/base.py:219](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L219)

Base class for multi-agent helpers.

This class integrates with existing Strands Agent instances and provides multi-agent orchestration capabilities.

**Attributes**:

-   `id` - Unique MultiAgent id for session management,etc.

#### \_\_init\_\_

```python
def __init__() -> None
```

Defined in: [src/strands/multiagent/base.py:235](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L235)

Initialize base multi-agent state.

#### invoke\_async

```python
@abstractmethod
async def invoke_async(task: MultiAgentInput,
                       invocation_state: dict[str, Any] | None = None,
                       **kwargs: Any) -> MultiAgentResult
```

Defined in: [src/strands/multiagent/base.py:273](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L273)

Invoke asynchronously.

**Arguments**:

-   `task` - The task to execute
-   `invocation_state` - Additional state/context passed to underlying agents. Defaults to None to avoid mutable default argument issues.
-   `**kwargs` - Additional keyword arguments passed to underlying agents.

#### stream\_async

```python
async def stream_async(task: MultiAgentInput,
                       invocation_state: dict[str, Any] | None = None,
                       **kwargs: Any) -> AsyncIterator[dict[str, Any]]
```

Defined in: [src/strands/multiagent/base.py:286](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L286)

Stream events during multi-agent execution.

Default implementation executes invoke\_async and yields the result as a single event. Subclasses can override this method to provide true streaming capabilities.

**Arguments**:

-   `task` - The task to execute
-   `invocation_state` - Additional state/context passed to underlying agents. Defaults to None to avoid mutable default argument issues.
-   `**kwargs` - Additional keyword arguments passed to underlying agents.

**Yields**:

Dictionary events containing multi-agent execution information including:

-   Multi-agent coordination events (node start/complete, handoffs)
-   Forwarded single-agent events with node context
-   Final result event

#### \_\_call\_\_

```python
def __call__(task: MultiAgentInput,
             invocation_state: dict[str, Any] | None = None,
             **kwargs: Any) -> MultiAgentResult
```

Defined in: [src/strands/multiagent/base.py:311](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L311)

Invoke synchronously.

**Arguments**:

-   `task` - The task to execute
-   `invocation_state` - Additional state/context passed to underlying agents. Defaults to None to avoid mutable default argument issues.
-   `**kwargs` - Additional keyword arguments passed to underlying agents.

#### serialize\_state

```python
def serialize_state() -> dict[str, Any]
```

Defined in: [src/strands/multiagent/base.py:331](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L331)

Return a JSON-serializable snapshot of the orchestrator state.

#### deserialize\_state

```python
def deserialize_state(payload: dict[str, Any]) -> None
```

Defined in: [src/strands/multiagent/base.py:335](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L335)

Restore orchestrator state from a session dict.

#### add\_hook

```python
def add_hook(callback: HookCallback,
             event_type: type | list[type] | None = None,
             *,
             order: float = HookOrder.DEFAULT) -> None
```

Defined in: [src/strands/multiagent/base.py:339](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/multiagent/base.py#L339)

Register a hook callback with the orchestrator.

Subclasses that support hooks should override this method to register the callback with their hook registry.

**Arguments**:

-   `callback` - The callback function to invoke when events of this type occur.
-   `event_type` - The class type(s) of events this callback should handle. Can be a single type, a list of types, or None to infer from the callback’s first parameter type hint.
-   `order` - Execution priority. Lower values execute first.