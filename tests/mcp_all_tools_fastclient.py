import asyncio

from fastmcp import Client


async def main():
    async with Client("http://localhost:8000/mcp") as client:

        # List available tools
        tools = await client.list_tools()

        print("\nAvailable Tools:")
        for tool in tools:
            print(f"- {tool.name}")

        # Health Tool
        print("\nCalling health tool...")
        health_result = await client.call_tool("health")

        print("Health Response:")
        print(health_result.data)

        # Say Hello Tool
        print("\nCalling say_hello tool...")
        hello_result = await client.call_tool(
            "say_hello",
            {"name": "Satheesh"}
        )

        print("Hello Response:")
        print(hello_result.data)

        # Generate UUID Tool
        print("\nCalling generate_uuid tool...")
        uuid_result = await client.call_tool("generate_uuid")

        print("UUID Response:")
        print(uuid_result.data)


if __name__ == "__main__":
    asyncio.run(main())