from scr.main import root, funcaoteste
from unittest.mock import patch


def test_root():
    assert root() == {"message": "helloworld"}


def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

