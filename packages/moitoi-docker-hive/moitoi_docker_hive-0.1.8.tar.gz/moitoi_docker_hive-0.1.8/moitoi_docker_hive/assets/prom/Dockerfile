FROM prom/prometheus:latest
COPY prometheus.yml /etc/prometheus/prometheus.yml
HEALTHCHECK --interval=5s --timeout=10s --retries=3 CMD curl -sS 127.0.0.1:9090 || exit 1
