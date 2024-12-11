FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install prometheus_client psutil

CMD ["python", "main.py"]