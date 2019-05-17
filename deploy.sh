#!/bin/bash
docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD 
docker tag bang_central twitchbambot/bang_central:latest
docker push twitchbambot/bang_central:latest
