#!/bin/sh
set -e
set +x
export TAG=$(git rev-parse HEAD)
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/l6a6l2j9
docker tag backendforst:latest public.ecr.aws/l6a6l2j9/backendforst:$TAG
docker push public.ecr.aws/l6a6l2j9/backendforst:$TAG
