from __future__ import annotations

import uuid
from datetime import UTC, datetime

from fastmcp import FastMCP

mcp = FastMCP(
    name="ProductionMCPServer",
    instructions=(
        "Production MCP server exposing health, hello, "
        "and UUID generation tools."
    ),
)


@mcp.tool(
    annotations={
        "title": "Health Check",
        "readOnlyHint": True,
        "idempotentHint": True,
    }
)
def health() -> dict:
    """
    Returns server health status.
    """
    return {
        "status": "healthy",
        "service": "ProductionMCPServer",
        "timestamp": datetime.now(UTC).isoformat(),
    }


@mcp.tool(
    annotations={
        "title": "Say Hello",
        "readOnlyHint": True,
        "idempotentHint": True,
    }
)
def say_hello(name: str) -> str:
    """
    Returns a greeting message.
    """
    cleaned_name = name.strip()
    return f"Hello {cleaned_name}! Welcome to FastMCP."


@mcp.tool(
    annotations={
        "title": "Generate UUID",
        "readOnlyHint": True,
    }
)
def generate_uuid() -> str:
    """
    Generates a random UUID4.
    """
    return str(uuid.uuid4())


if __name__ == "__main__":
    mcp.run()