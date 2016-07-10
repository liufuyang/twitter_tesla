#!/bin/sh
eval $(docker-machine env default)

./local_build.sh

docker stop twitter-tesla-webservice
docker rm twitter-tesla-webservice

docker run -p 8080:8080 --name twitter-tesla-webservice \
	-e "DB_HOST=192.168.99.100" \
	-e "DB_PORT=5435" \
	-e "DB_USER=postgres" \
	-e "DB_PASS=password" \
	-e "DB_NAME=twitter_tesla" \
	-v /Users/fuyangliu/Workspace/twitter_tesla/z_log/ws1:/var/www/app/log \
	-v /Users/fuyangliu/Workspace/twitter_tesla/z_log/ws2:/var/log/uwsgi/app \
	liufuyang/twitter-tesla-webservice:latest 
