#!/bin/sh
set -e
set +x
export TAG=$(git rev-parse HEAD)
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/l6a6l2j9
cd backend && docker build -t backendforst:latest .
docker tag backendforst:latest public.ecr.aws/l6a6l2j9/backendforst:$TAG
docker push public.ecr.aws/l6a6l2j9/backendforst:$TAG
cd ..
ecs-cli configure --cluster Todot --default-launch-type EC2 --region eu-central-1 --config-name configuration
ls
ecs-cli compose --project-name todot_backend --file td.yml create
export TaskDefinition=$(aws ecs list-task-definitions --family-prefix  todot_backend --region eu-central-1  | jq -r .taskDefinitionArns[-1] )
aws ecs update-service --cluster Todot --service todot_service --force-new-deployment --region eu-central-1 --task-definition $TaskDefinition
#| sed 's/.*\///'
export RolloutState=$(aws ecs describe-services --cluster Todot --service todot_service | jq -r .services[].deployments[] | jq -r .rolloutState))
until $(aws ecs describe-services --cluster Todot --service todot_service | jq -r .services[].deployments[] | jq -r .rolloutState)) == "COMPLETED"
do
  sleep 5
  echo "Deployment in progress"
done
