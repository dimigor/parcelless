#!/bin/bash

heroku_app="parcelless"

docker build -t registry.heroku.com/$heroku_app/web --target prod --platform linux/amd64 .

docker push registry.heroku.com/$heroku_app/web

heroku container:release web --app=$heroku_app
