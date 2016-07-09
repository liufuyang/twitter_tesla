#!/bin/sh
eval $(docker-machine env default)

./local_build.sh

docker stop twitter-tesla-webservice
docker rm twitter-tesla-webservice

docker run -p 8080:8080 --name twitter-tesla-webservice liufuyang/twitter-tesla-webservice:latest 
