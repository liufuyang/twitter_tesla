#!/bin/bash
eval $(docker-machine env default)

DEPLOY_DIR=z_local_deploy
rm -rf ./${DEPLOY_DIR}
mkdir ${DEPLOY_DIR}
cp -R local_dev/* ${DEPLOY_DIR}

# docker_webservice
cp -R app ${DEPLOY_DIR}/docker_webservice/app

docker build --no-cache -t liufuyang/twitter-tesla-webservice:latest ${DEPLOY_DIR}/docker_webservice

# docker_twitter_gen
cp -R twitter_gen ${DEPLOY_DIR}/docker_twitter_gen/twitter_gen

docker build --no-cache -t liufuyang/twitter-tesla-tgen:latest ${DEPLOY_DIR}/docker_twitter_gen
