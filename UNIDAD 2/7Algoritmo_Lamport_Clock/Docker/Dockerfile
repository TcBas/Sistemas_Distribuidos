FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Copiar las dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "lamport_clock.py"]
