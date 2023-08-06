FROM akepler/mdh_base:latest

MAINTAINER Andres Kepler <andres@kepler.ee>

COPY requirements.txt /app/requirements.txt
COPY start.sh /app/start.sh

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

HEALTHCHECK --interval=5s --timeout=10s --retries=3 CMD curl -sS 127.0.0.1:5000 || exit 1

ENTRYPOINT  ["/bin/sh"]

CMD ["/app/start.sh"]
