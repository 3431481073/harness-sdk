Python REPL tool: run Python through a sandbox.

Provides :func:`make_python_repl` (a factory for a sandbox-routed Python tool) and :data:`python_repl` (the default instance that uses the agent’s sandbox). Each call pipes the code to a fresh interpreter process in the sandbox, so variables, imports, and definitions do not persist across calls. Files written to the sandbox filesystem persist for as long as the sandbox does, so code can checkpoint intermediate results to disk.

#### make\_python\_repl

```python
def make_python_repl(
        *,
        sandbox: Sandbox | None = None,
        name: str = "python_repl",
        description: str = PYTHON_REPL_DESCRIPTION,
        language: str = _DEFAULT_LANGUAGE) -> DecoratedFunctionTool
```

Defined in: [src/strands/vended\_tools/python\_repl/python\_repl.py:30](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/vended_tools/python_repl/python_repl.py#L30)

Create a sandbox-routed Python REPL tool.

If a `sandbox` is passed, it is bound at creation time. Otherwise the tool reads the sandbox from `tool_context.agent.sandbox` at call time.

**Arguments**:

-   `sandbox` - Sandbox to bind at creation. When `None`, the agent’s configured sandbox is used at call time.
-   `name` - Tool name. Defaults to `"python_repl"`.
-   `description` - Tool description shown to the model.
-   `language` - Python interpreter used to run the code. Defaults to `"python3"`.

**Returns**:

A decorated tool that executes Python code through the sandbox.

**Raises**:

-   `ValueError` - If `name` is empty or `language` contains invalid characters.

#### python\_repl

Default Python REPL tool. Reads the sandbox from the agent’s context at call time.