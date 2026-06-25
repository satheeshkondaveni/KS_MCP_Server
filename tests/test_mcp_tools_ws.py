import uuid

from app.server_ws import (
    generate_uuid,
    health,
    say_hello,
)


def test_health():
    result = health()

    assert isinstance(result, dict)
    assert result["status"] == "healthy"
    assert result["service"] == "ProductionMCPServer"
    assert "timestamp" in result


def test_say_hello():
    result = say_hello("Satheesh")

    assert result == "Hello Satheesh! Welcome to FastMCP."


def test_generate_uuid():
    value = generate_uuid()

    parsed = uuid.UUID(value)

    assert isinstance(parsed, uuid.UUID)
    assert str(parsed) == value