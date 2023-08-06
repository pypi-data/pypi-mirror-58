FROM akepler/mdh_base:latest

COPY requirements.txt /app/requirements.txt
COPY start.sh /app/start.sh

WORKDIR /app

RUN pip install --no-cache-dir  -r requirements.txt

COPY . .

VOLUME /var/run/docker.sock

HEALTHCHECK --interval=5s --timeout=10s --retries=3 CMD curl -sS 127.0.0.1:5000 || exit 1

ENTRYPOINT  ["/bin/sh"]

CMD ["/app/start.sh"]
