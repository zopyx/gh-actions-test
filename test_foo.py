
from foo import hello, world

def test_hello():
    result = hello()
    assert result == "world"


def test_world():
    result = world()
    assert result == "hello"

