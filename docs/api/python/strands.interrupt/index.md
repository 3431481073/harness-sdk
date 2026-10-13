Human-in-the-loop interrupt system for agent workflows.

## Interrupt

```python
@dataclass
class Interrupt()
```

Defined in: [src/strands/interrupt.py:17](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L17)

Represents an interrupt that can pause agent execution for human-in-the-loop workflows.

**Attributes**:

-   `id` - Unique identifier. Treat as opaque: pass it back to resume the agent, do not parse or construct it.
-   `name` - User defined name.
-   `reason` - User provided reason for raising the interrupt.
-   `response` - Human response provided when resuming the agent after an interrupt.

#### to\_dict

```python
def to_dict() -> dict[str, Any]
```

Defined in: [src/strands/interrupt.py:33](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L33)

Serialize to dict for session management.

## InterruptException

```python
class InterruptException(Exception)
```

Defined in: [src/strands/interrupt.py:38](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L38)

Exception raised when human input is required.

#### \_\_init\_\_

```python
def __init__(interrupt: Interrupt) -> None
```

Defined in: [src/strands/interrupt.py:41](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L41)

Set the interrupt.

## PendingToolExecution

```python
@dataclass
class PendingToolExecution()
```

Defined in: [src/strands/interrupt.py:47](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L47)

State required to resume tool execution without calling the model again.

**Attributes**:

-   `assistant_message` - Assistant message containing the pending tool uses.
-   `completed_tool_results` - Results completed or synthesized during the interrupted execution.

## \_InterruptState

```python
@dataclass
class _InterruptState()
```

Defined in: [src/strands/interrupt.py:60](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L60)

Track the state of interrupt events raised by the user.

Note, unanswered interrupts are cleared after resuming; an answered invocation-scoped response is retained for the rest of its interrupt cycle.

**Attributes**:

-   `interrupts` - Interrupts raised by the user. May be non-empty even when `activated` is False because retained responses persist until their cycle ends.
-   `context` - Additional context associated with an interrupt event.
-   `activated` - True if agent is in an interrupt state, False otherwise.
-   `pending_tool_execution` - State required to resume an interrupted tool execution.

#### activate

```python
def activate() -> None
```

Defined in: [src/strands/interrupt.py:80](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L80)

Activate the interrupt state.

#### deactivate

```python
def deactivate() -> None
```

Defined in: [src/strands/interrupt.py:85](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L85)

Deactivate the interrupt state.

Interrupts, context, and pending tool execution are cleared.

#### end\_tool\_cycle

```python
def end_tool_cycle() -> None
```

Defined in: [src/strands/interrupt.py:96](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L96)

Clear a completed tool cycle’s state, keeping answered invocation-scoped responses.

#### end\_interrupt\_cycle

```python
def end_interrupt_cycle() -> None
```

Defined in: [src/strands/interrupt.py:108](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L108)

Release invocation-scoped interrupts once their interrupt cycle is over.

#### resume

```python
def resume(prompt: "AgentInput") -> None
```

Defined in: [src/strands/interrupt.py:121](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L121)

Configure the interrupt state if resuming from an interrupt event.

**Arguments**:

-   `prompt` - User responses if resuming from interrupt.

**Raises**:

-   `TypeError` - If in interrupt state but user did not provide responses.

#### set\_pending\_tool\_results

```python
def set_pending_tool_results(
        completed_tool_results: list["ToolResult"]) -> None
```

Defined in: [src/strands/interrupt.py:157](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L157)

Update completed results for a pending tool execution.

#### to\_dict

```python
def to_dict() -> dict[str, Any]
```

Defined in: [src/strands/interrupt.py:178](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L178)

Serialize to dict for session management.

Exclude deactivated invocation-scoped responses — persisting them would give a restored agent a standing approval.

#### from\_dict

```python
@classmethod
def from_dict(cls, data: dict[str, Any]) -> "_InterruptState"
```

Defined in: [src/strands/interrupt.py:202](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/interrupt.py#L202)

Initialize interrupt state from serialized interrupt state.

Interrupt state can be serialized with the `to_dict` method. Legacy tool execution context is migrated into the typed pending state.