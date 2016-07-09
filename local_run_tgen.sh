#!/bin/sh
eval $(docker-machine env default)

./local_build.sh

docker stop twitter-tesla-tgen
docker rm twitter-tesla-tgen

docker run --name twitter-tesla-tgen liufuyang/twitter-tesla-tgen:latest
