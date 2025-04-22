FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y libaio1 unzip curl gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY src /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
