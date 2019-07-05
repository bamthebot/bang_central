#!/bin/bash
source .env
docker-compose -f docker-compose.prod.yaml kill
docker-compose -f docker-compose.prod.yaml rm -f
docker-compose -f docker-compose.prod.yaml up -d
