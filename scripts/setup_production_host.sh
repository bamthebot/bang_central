#!/bin/bash
PRODUCTION_HOST=$1
BANG_CENTRAL_PATH="/home/ubuntu/bang_central/"
cd ..
echo "Setting up repo at $PRODUCTION_HOST"
ssh ubuntu@$PRODUCTION_HOST "rm -rf $BANG_CENTRAL_PATH"
ssh ubuntu@$PRODUCTION_HOST "git clone git@github.com:bamthebot/bang_central.git $BANG_CENTRAL_PATH"
echo "Initializing server at $PRODUCTION_HOST"
scp .env ubuntu@$PRODUCTION_HOST:/home/ubuntu/bang_central/.env
ssh ubuntu@$PRODUCTION_HOST "cd $BANG_CENTRAL_PATH && ./init.sh"
