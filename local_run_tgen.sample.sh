#!/bin/sh
eval $(docker-machine env default)

./local_build.sh

docker stop twitter-tesla-tgen
docker rm twitter-tesla-tgen

echo "Start docker container twitter-tesla-tgen in 5 seconds ..."
sleep 5

docker run --name twitter-tesla-tgen \
	-e "TW_CONSUMER_KEY=*****" \
	-e "TW_CONSUMER_SECRET=*****" \
	-e "TW_ACCESS_TOKEN=*****" \
	-e "TW_ACCESS_SECRET=*****" \
	-e "DB_HOST=192.168.99.100" \
	-e "DB_PORT=5435" \
	-e "DB_USER=postgres" \
	-e "DB_PASS=password" \
	-e "DB_NAME=twitter_tesla" \
	-e "TW_QUERY_1=tesla" \
	-e "TW_QUERY_2=TeslaMotors" \
	-v /Users/log:/twitter_gen/log \
	liufuyang/twitter-tesla-tgen:latest

# http://stackoverflow.com/questions/31249112/allow-docker-container-to-connect-to-a-local-host-postgres-database
