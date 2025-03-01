#!/bin/sh

#ls -R app/
flask --app app/source/main.py run --debug


exec "$@"