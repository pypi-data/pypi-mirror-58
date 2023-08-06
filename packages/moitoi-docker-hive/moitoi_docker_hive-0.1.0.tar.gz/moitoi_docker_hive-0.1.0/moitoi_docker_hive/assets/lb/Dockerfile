FROM akepler/mdh_base:latest

MAINTAINER Andres Kepler <andres@kepler.ee>

ENV LANG C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
		gnupg2 \
		curl \
		wget

RUN wget -qO- https://nginx.org/keys/nginx_signing.key | apt-key add -
RUN echo "deb http://nginx.org/packages/debian/ buster nginx" | tee /etc/apt/sources.list.d/nginx.list
RUN apt-get update && apt-get install -y --no-install-recommends \
		nginx \
	&& rm -rf /var/lib/apt/lists/*


VOLUME ["/data"]
COPY nginx.conf /data/etc/nginx/nginx.conf
COPY 502.html /data/www/assets/502.html
COPY 502.html /data/www/index.html
COPY start.sh /app/start.sh
COPY start_nginx.sh /app/start_nginx.sh
COPY telegraf.conf /app/telegraf.conf


HEALTHCHECK --interval=5s --timeout=10s --retries=3 CMD curl -sS 127.0.0.1:5000 || exit 1

ENTRYPOINT  ["/bin/sh"]

CMD ["/app/start.sh"]
