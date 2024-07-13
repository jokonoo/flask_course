#!/bin/bash

sleep 5
flask db upgrade
pytest

tail -f /dev/null