#!/usr/bin/env bash
cd /app
/usr/local/bin/gunicorn --logger-class gunicorn.instrument.statsd.Statsd --statsd-host=mdh_statsd:9125 --log-level debug --statsd-prefix=mdh.$1 -w 2 -b :5000 app:app
