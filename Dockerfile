FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt found, continuing..."

CMD ["python", "main.py"]
