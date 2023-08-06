FROM grafana/grafana:latest
COPY --chown=grafana grafana.ini /etc/grafana/grafana.ini
COPY --chown=grafana datasource.yml /etc/grafana/provisioning/datasources/datasource.yml
COPY --chown=grafana dashboard.yml /etc/grafana/provisioning/dashboards/dashboard.yml
COPY --chown=grafana dashboard.json /var/lib/grafana/dashboards/dashboard.json
