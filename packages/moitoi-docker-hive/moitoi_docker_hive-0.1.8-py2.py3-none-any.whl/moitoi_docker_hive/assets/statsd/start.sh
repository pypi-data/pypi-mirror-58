#!/bin/bash
cd /app
/bin/statsd_exporter --statsd.mapping-config=/app/statsd.conf
