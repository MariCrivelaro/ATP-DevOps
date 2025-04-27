from scr.main import root, funcaoteste
from unittest.mock import patch
import pytest

# Teste 1 - Teste assíncrono para root
@pytest.mark.asyncio
async def test_root():
    result = await root()  # Usando await para aguardar a execução da coroutine
    assert result == {"message": "helloworld"}

# Teste 2 - Teste assíncrono para funcaoteste
@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()  # Usando await para aguardar a execução da coroutine
    assert result == {"teste": True, "num_aleatorio": 12345}

# Teste 3 - Testar se root retorna um dicionário
@pytest.mark.asyncio
async def test_root_type():
    result = await root()  # Usando await para aguardar a execução da coroutine
    assert isinstance(result, dict)

# Teste 4 - Testar se funcaoteste gera um número aleatório diferente de None
@pytest.mark.asyncio
async def test_funcaoteste_random():
    result = await funcaoteste()  # Usando await para aguardar a execução da coroutine
    assert result["num_aleatorio"] is not None

# Teste 5 - Testar se a chave 'teste' existe no retorno de funcaoteste
@pytest.mark.asyncio
async def test_funcaoteste_has_key():
    result = await funcaoteste()  # Usando await para aguardar a execução da coroutine
    assert "teste" in result
