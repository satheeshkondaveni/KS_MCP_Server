import asyncio
from fastmcp import Client


async def main():
    async with Client("http://localhost:8000/mcp") as client:

        result = await client.call_tool(
            "say_hello",
            {"name": "Satheesh"}
        )

        print("data =", result.data)
        print("structured =", result.structured_content)

        if result.data:
            print(result.data["message"])


asyncio.run(main())