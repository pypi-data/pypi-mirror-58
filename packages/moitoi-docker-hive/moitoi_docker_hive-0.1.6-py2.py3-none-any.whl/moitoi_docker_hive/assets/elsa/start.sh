#!/bin/bash
cd /app
set -m
chmod 755 /app/start_telegraf.sh
./start_telegraf.sh &
chmod 755 /app/start_gunicorn.sh
./start_gunicorn.sh $MDH_HOSTNAME
fg %1
