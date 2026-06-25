You can use the following production-style `README.md` for your FastMCP server and client applications.

# FastMCP Tools Server

A production-ready FastMCP server exposing the following tools:

* `health` - Health check endpoint
* `say_hello` - Returns a greeting message
* `generate_uuid` - Generates a random UUID

## Project Structure

```text
project/
│
├── app/
│   ├── __init__.py
│   └── server.py
│
├── client/
│   └── mcp_client.py
│
├── tests/
│   └── test_mcp_tools.py
│
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Prerequisites

* Python 3.14+
* pip

Verify installation:

```bash
python --version
```

Expected:

```text
Python 3.14.x
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install fastmcp pytest pytest-asyncio
```

---

## Start MCP Server

Navigate to the project root folder.

Run:

```bash
python app/server.py
```

Expected output:

```text
INFO: FastMCP server started
INFO: Listening on http://0.0.0.0:8000/mcp
```

---

## Verify Server

Open a new terminal and run:

```bash
curl http://localhost:8000/mcp
```

or

```bash
fastmcp list http://localhost:8000/mcp
```

Expected tools:

```text
health
say_hello
generate_uuid
```

---

## Run Client Application

Example:

```bash
python client/mcp_client.py
```

Expected output:

```text
Available Tools:
- health
- say_hello
- generate_uuid

Health Response:
{'status': 'healthy'}

Hello Response:
{'message': 'Hello Satheesh'}

UUID Response:
{'uuid': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'}
```

---

## Example Client Code

```python
import asyncio

from fastmcp import Client


async def main():
    async with Client("http://localhost:8000/mcp") as client:

        health = await client.call_tool("health")
        print(health.data)

        hello = await client.call_tool(
            "say_hello",
            {"name": "Satheesh"}
        )
        print(hello.data)

        uuid_result = await client.call_tool(
            "generate_uuid"
        )
        print(uuid_result.data)


if __name__ == "__main__":
    asyncio.run(main())
```

---

## Run Tests

Execute:

```bash
pytest -v
```

Expected:

```text
tests/test_mcp_tools.py::test_health PASSED
tests/test_mcp_tools.py::test_say_hello PASSED
tests/test_mcp_tools.py::test_generate_uuid PASSED
```

---

## Available Tools

### health

Request:

```python
await client.call_tool("health")
```

Response:

```json
{
  "status": "healthy"
}
```

### say_hello

Request:

```python
await client.call_tool(
    "say_hello",
    {
        "name": "Satheesh"
    }
)
```

Response:

```json
{
  "message": "Hello Satheesh"
}
```

### generate_uuid

Request:

```python
await client.call_tool(
    "generate_uuid"
)
```

Response:

```json
{
  "uuid": "550e8400-e29b-41d4-a716-446655440000"
}
```

---

## Troubleshooting

### List Tools Works but Tool Returns None

Verify the server returns a dictionary:

```python
@mcp.tool
def say_hello(name: str) -> dict:
    return {
        "message": f"Hello {name}"
    }
```

Avoid returning primitive values such as strings for production APIs.

### Connection Refused

Ensure the MCP server is running:

```bash
python app/server.py
```

Verify port:

```bash
netstat -ano | findstr 8000
```

### Verify FastMCP Version

```bash
pip show fastmcp
```

Recommended:

```text
fastmcp >= 3.x
```

---

## Production Recommendations

* Run behind Nginx or API Gateway.
* Enable HTTPS.
* Add authentication and authorization.
* Use structured responses (dict/Pydantic models).
* Add logging and monitoring.
* Deploy with Docker/Kubernetes.
* Add retry and timeout handling in clients.

---

## License

MIT License

This README should be sufficient for onboarding developers, running the server/client locally, and validating the MCP tools end-to-end.
