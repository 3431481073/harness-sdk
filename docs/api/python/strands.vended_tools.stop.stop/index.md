Tool for gracefully ending the agent loop.

Provides :func:`make_stop` (a factory for customized stop tools) and :data:`stop` (the default instance). The tool calls `agent.cancel(message=..., after_current_tools=True)`: any sibling tools in the same batch run to completion, then the loop exits with `stop_reason == "cancelled"` and the message as the final assistant message. The same message is returned as the tool result the model sees for its stop request.

#### DEFAULT\_MAX\_MESSAGE\_LENGTH

Default cap on the stop `message` length. The cap exists so a runaway model can’t blow the conversation history in one shot; adjust via `make_stop(max_message_length=...)` when a longer summary is legitimate.

#### make\_stop

```python
def make_stop(
    *,
    name: str = "stop",
    description: str = DEFAULT_STOP_DESCRIPTION,
    max_message_length: int = DEFAULT_MAX_MESSAGE_LENGTH
) -> DecoratedFunctionTool
```

Defined in: [src/strands/vended\_tools/stop/stop.py:56](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/vended_tools/stop/stop.py#L56)

Create a stop tool that gracefully ends the agent loop.

The tool calls `agent.cancel(message=..., after_current_tools=True)` so the loop ends after the current tool batch without invoking the model again.

**Arguments**:

-   `name` - Tool name. Defaults to `"stop"`.
-   `description` - Tool description shown to the model.
-   `max_message_length` - Maximum accepted length for the model-supplied `message` argument, in characters. Must be a positive integer. Defaults to :data:`DEFAULT_MAX_MESSAGE_LENGTH` (4096).

**Returns**:

A decorated tool that signals the event loop to stop after the current tool batch completes.

**Raises**:

-   `ValueError` - If `max_message_length` is not a positive integer.

#### stop

Default stop tool. Ends the agent loop when called by the model.