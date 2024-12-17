# Usa una imagen base de Python
FROM python:3.9-slim

# Instala las dependencias necesarias
RUN pip install requests

# Copia el código al contenedor
COPY client.py /app/client.py

# Define el directorio de trabajo
WORKDIR /app

# Comando para ejecutar el cliente
CMD ["python", "client.py"]
