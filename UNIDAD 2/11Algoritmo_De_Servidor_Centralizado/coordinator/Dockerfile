FROM python:3.9-slim

WORKDIR /app

COPY coordinator.py .

RUN pip install flask

CMD ["python", "coordinator.py"]
