#!/bin/bash
TAG=$1

# Build
cd ..
docker build . -t bang_central

# Push
docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD 
docker tag bang_central twitchbambot/bang_central:$TAG
docker push twitchbambot/bang_central:$TAG
