#!/bin/bash
cd /app
set -m
chmod 755 /app/start_telegraf.sh
./start_telegraf.sh &
chmod 755 /app/start_nginx.sh
./start_nginx.sh
fg %1
