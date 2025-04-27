from scr.main import root, funcaoteste
from unittest.mock import patch
import pytest

# Teste 1
def test_root():
    assert root() == {"message": "helloworld"}

# Teste 2
def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

# Teste 3 - Testar se root retorna um dicionário
def test_root_type():
    result = root()
    assert isinstance(result, dict)

# Teste 4 - Testar se funcaoteste gera um número aleatório diferente de None
def test_funcaoteste_random():
    result = funcaoteste()
    assert result["num_aleatorio"] is not None

# Teste 5 - Testar se a chave 'teste' existe no retorno de funcaoteste
def test_funcaoteste_has_key():
    result = funcaoteste()
    assert "teste" in result
