#!/bin/bash

sleep 10
flask db upgrade
flask run --host 0.0.0.0 --port 8080

tail -f /dev/null