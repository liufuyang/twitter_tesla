#!/bin/sh
eval $(docker-machine env default)

DEPLOY_DIR=z_local_deploy
rm -rf ./${DEPLOY_DIR}
mkdir ${DEPLOY_DIR}
cp -R local_dev/* ${DEPLOY_DIR}

docker build --no-cache -t liufuyang/flask:latest ${DEPLOY_DIR}/docker_flask

docker login
docker push liufuyang/flask:latest
