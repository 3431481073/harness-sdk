Shared types and constants for the Python REPL tool.

## PythonReplOutput

```python
class PythonReplOutput(TypedDict)
```

Defined in: [src/strands/vended\_tools/python\_repl/types.py:6](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/vended_tools/python_repl/types.py#L6)

Output of a Python REPL execution.

**Attributes**:

-   `output` - Standard output captured from the interpreter.
-   `error` - Standard error captured from the interpreter, including tracebacks. Empty when there was none.
-   `exit_code` - Exit code of the interpreter. Non-zero means the code failed.

## PythonReplError

```python
class PythonReplError(RuntimeError)
```

Defined in: [src/strands/vended\_tools/python\_repl/types.py:20](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/vended_tools/python_repl/types.py#L20)

Raised when the sandbox fails to run the Python code.

Raised for sandbox-level failures (for example, an unreachable container), not for errors in the code itself; those are reported through `error` and a non-zero `exit_code`. Subclasses :class:`RuntimeError` so existing `except RuntimeError` handlers keep working.

#### PYTHON\_REPL\_DESCRIPTION

Description for the Python REPL tool.