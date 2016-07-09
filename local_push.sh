#!/bin/sh
eval $(docker-machine env default)

docker login
docker push liufuyang/twitter-tesla-webservice:latest
