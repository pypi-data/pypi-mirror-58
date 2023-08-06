#!/usr/bin/env bash
cd /app
nginx -c /data/etc/nginx/nginx.conf -g "daemon off;"
