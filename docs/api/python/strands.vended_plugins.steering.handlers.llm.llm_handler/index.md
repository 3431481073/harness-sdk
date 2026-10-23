LLM-based steering handler that uses an LLM to provide contextual guidance.

## LLMSteeringHandler

```python
class LLMSteeringHandler(SteeringHandler)
```

Defined in: [src/strands/vended\_plugins/steering/handlers/llm/llm\_handler.py:34](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/vended_plugins/steering/handlers/llm/llm_handler.py#L34)

Steering handler that uses an LLM to provide contextual guidance.

Uses natural language prompts to evaluate tool calls and provide contextual steering guidance to help agents navigate complex workflows.

#### \_\_init\_\_

```python
def __init__(system_prompt: str,
             prompt_mapper: LLMPromptMapper | None = None,
             model: Model | None = None,
             context_providers: list[SteeringContextProvider] | None = None)
```

Defined in: [src/strands/vended\_plugins/steering/handlers/llm/llm\_handler.py:41](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/vended_plugins/steering/handlers/llm/llm_handler.py#L41)

Initialize the LLMSteeringHandler.

**Arguments**:

-   `system_prompt` - System prompt defining steering guidance rules
-   `prompt_mapper` - Custom prompt mapper for evaluation prompts
-   `model` - Model for steering evaluation. Resolution order: this `model` > `agent.aux_model` > `agent.model`.
-   `context_providers` - List of context providers for populating steering context. Defaults to \[LedgerProvider()\] if None. Pass an empty list to disable context providers.

#### steer\_before\_tool

```python
async def steer_before_tool(*,
                            agent: Agent,
                            tool_use: ToolUse,
                            invocation_context: InvocationContext
                            | None = None,
                            **kwargs: Any) -> ToolSteeringAction
```

Defined in: [src/strands/vended\_plugins/steering/handlers/llm/llm\_handler.py:67](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/vended_plugins/steering/handlers/llm/llm_handler.py#L67)

Provide contextual guidance for tool usage.

**Arguments**:

-   `agent` - The agent instance
-   `tool_use` - The tool use object with name and arguments
-   `invocation_context` - The request this tool call belongs to; the steering call’s usage adds to it.
-   `**kwargs` - Additional keyword arguments for steering evaluation

**Returns**:

SteeringAction indicating how to guide the tool execution