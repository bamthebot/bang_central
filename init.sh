#!/bin/bash
source .env
docker-compose -d -f docker-compose.prod.yaml up
