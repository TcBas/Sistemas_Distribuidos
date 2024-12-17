FROM python:3.8-slim

WORKDIR /app

COPY coordinator.py /app/

RUN pip install flask  # Si necesitas un servidor web

CMD ["python", "coordinator.py"]
