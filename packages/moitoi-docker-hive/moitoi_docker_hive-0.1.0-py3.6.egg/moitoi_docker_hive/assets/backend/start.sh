#!/bin/bash
cd /app
set -m

chmod 755 /app/start_telegraf.sh
/app/start_telegraf.sh &
chmod 755 /app/start_gunicorn.sh
/app/start_gunicorn.sh $MDH_HOSTNAME

fg %1
