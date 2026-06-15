import pytest
from tds_hello_vineetha import greet, shout

def test_default():
    assert greet() == "Hello, world! — from tds-hello v0.2.0"

def test_custom_name():
    assert "Alice" in greet("Alice")

def test_invalid_type():
    with pytest.raises(TypeError):
        greet(42)  # type: ignore[arg-type]
def test_shout():
    assert shout("Alice") == greet("Alice").upper()
