#!/bin/bash
PRODUCTION_HOST=$1
BANG_CENTRAL_PATH="/home/ubuntu/bang_central/"
cd ..
ssh ubuntu@$PRODUCTION_HOST "rm -rf $BANG_CENTRAL_PATH"
ssh ubuntu@$PRODUCTION_HOST "git clone git@github.com:bamthebot/bang_central.git $BANG_CENTRAL_PATH"
scp .env ubuntu@$PRODUCTION_HOST:/home/ubuntu/bang_central/.env
ssh ubuntu@$PRODUCTION_HOST "cd $BANG_CENTRAL_PATH && init.sh"
