#!/bin/sh
eval $(docker-machine env default)

docker stop twitter-tesla-postgres
docker rm twitter-tesla-postgres

docker run --name twitter-tesla-postgres -d \
	-e POSTGRES_PASSWORD=password \
	-e POSTGRES_USER=postgres \
	-e POSTGRES_DB=twitter_tesla \
	-p 5435:5432 \
	-d postgres:9.3
