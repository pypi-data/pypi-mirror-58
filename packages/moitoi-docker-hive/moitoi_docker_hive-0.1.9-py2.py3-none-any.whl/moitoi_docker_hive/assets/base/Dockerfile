FROM python:buster

MAINTAINER Andres Kepler <andres@kepler.ee>

ENV LANG C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
		gnupg2 \
		curl \
		wget

RUN wget -qO- https://repos.influxdata.com/influxdb.key | apt-key add -
RUN echo "deb https://repos.influxdata.com/debian buster stable" | tee /etc/apt/sources.list.d/influxdb.list
# extra dependencies (over what buildpack-deps already includes)
RUN apt-get update && apt-get install -y --no-install-recommends \
		telegraf \
	&& rm -rf /var/lib/apt/lists/*

COPY telegraf.conf /app/telegraf.conf
COPY start.sh /app/start.sh
COPY start_telegraf.sh /app/start_telegraf.sh

WORKDIR /app

ENTRYPOINT  ["/bin/sh"]

CMD ["/app/start.sh"]
