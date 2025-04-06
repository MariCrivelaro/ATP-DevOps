FROM python:3

WORKDIR /usr/src/app

# Copia e instala as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Expõe a porta 80 para o container
EXPOSE 80

# Comando para rodar o servidor FastAPI com uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
