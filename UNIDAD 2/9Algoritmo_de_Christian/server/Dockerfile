# Usa una imagen base de Python
FROM python:3.9-slim

# Instala las dependencias necesarias
RUN pip install flask

# Copia el código al contenedor
COPY server.py /app/server.py

# Define el directorio de trabajo
WORKDIR /app

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar el servidor
CMD ["python", "server.py"]
