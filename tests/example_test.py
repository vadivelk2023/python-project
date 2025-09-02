from src import example
import pytest
def test_main():
    assert "Hello from pylearn" == example.main()

def test_f():
    with pytest.raises(SystemExit):
        example.f()