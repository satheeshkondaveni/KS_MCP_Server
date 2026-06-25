from fastmcp import FastMCP
from uuid import uuid4

mcp = FastMCP("my-tools")


@mcp.tool
def health() -> dict:
    return {
        "status": "healthy"
    }


@mcp.tool
def say_hello(name: str) -> dict:
    return {
        "message": f"Hello {name}"
    }


@mcp.tool
def generate_uuid() -> dict:
    return {
        "uuid": str(uuid4())
    }


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )