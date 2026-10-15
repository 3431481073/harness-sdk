"""Agent tool interfaces and utilities.

This module provides the core functionality for creating, managing, and executing tools through agents.
"""

from .decorator import tool
from .stop import make_stop, stop
from .structured_output import convert_pydantic_to_tool_spec
from .tool_provider import ToolProvider
from .tools import InvalidToolUseNameException, PythonAgentTool, normalize_schema, normalize_tool_spec

__all__ = [
    "tool",
    "PythonAgentTool",
    "InvalidToolUseNameException",
    "normalize_schema",
    "normalize_tool_spec",
    "convert_pydantic_to_tool_spec",
    "ToolProvider",
    "make_stop",
    "stop",
]
