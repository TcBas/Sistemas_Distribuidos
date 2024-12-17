# Imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos al contenedor
COPY lamport_clock.py /app/lamport_clock.py
COPY requirements.txt /app/requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar el archivo Python cuando el contenedor se ejecute
CMD ["python", "lamport_clock.py"]
