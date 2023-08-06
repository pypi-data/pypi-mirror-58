FROM prom/statsd-exporter:latest
COPY start.sh /app/start.sh
COPY statsd.conf /app/statsd.conf
WORKDIR /app
ENTRYPOINT  ["/bin/sh"]

CMD ["/app/start.sh"]
