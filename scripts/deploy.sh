#!/bin/bash
TAG=$1
docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD 
docker tag bang_central twitchbambot/bang_central:$TAG
docker push twitchbambot/bang_central:$TAG
