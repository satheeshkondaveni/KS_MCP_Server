import httpx
import asyncio
import json

async def sse_request(payload):
    headers = {"Accept": "application/json, text/event-stream"}
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("POST", "http://localhost:8080/mcp",
                                 headers=headers, json=payload) as r:
            async for line in r.aiter_lines():
                if line.startswith("data:"):
                    data = line[len("data:"):].strip()
                    if data:
                        yield json.loads(data)

async def main():
    # Step 1: Initialize session
    init_payload = {
        "jsonrpc": "2.0",
        "id": "init",
        "method": "initialize",
        "params": {
            "capabilities": {},   # required
            "clientInfo": {       # required
                "name": "TestClient",
                "version": "0.1"
            }
        }
    }

    session_id = None
    async for event in sse_request(init_payload):
        print("Init:", event)
        if "result" in event and "sessionId" in event["result"]:
            session_id = event["result"]["sessionId"]
            break

    if not session_id:
        raise RuntimeError("Failed to initialize session")

    # Step 2: Call tools
    async def call_tool(name, args=None):
        payload = {
            "jsonrpc": "2.0",
            "id": name,
            "method": "call_tool",
            "params": {
                "sessionId": session_id,
                "name": name,
                "arguments": args or {}
            }
        }
        async for event in sse_request(payload):
            return event

    print("Health:", await call_tool("health"))
    print("Say Hello:", await call_tool("say_hello", {"name": "Satheesh"}))
    print("UUID64:", await call_tool("generate_uuid"))

if __name__ == "__main__":
    asyncio.run(main())
