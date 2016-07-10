#!/bin/sh
eval $(docker-machine env default)

./local_build.sh

docker stop twitter-tesla-tgen
docker rm twitter-tesla-tgen

docker run --name twitter-tesla-tgen \
	-e "TW_CONSUMER_KEY=*****" \
	-e "TW_CONSUMER_SECRET=*****" \
	-e "TW_ACCESS_TOKEN=*****" \
	-e "TW_ACCESS_SECRET=*****" \
	liufuyang/twitter-tesla-tgen:latest
