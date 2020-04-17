#!/bin/sh

JQ="jq --raw-output --exit-status"

configure_aws_cli() {
  aws --version
  aws configure set default.region us-east-1
  aws configure set default.output json
  echo "AWS Configured!"
}

register_definition() {
  if revision=$(aws ecs register-task-definition --cli-input-json "$task_def" | $JQ '.taskDefinition.taskDefinitionArn'); then
    echo "Revision: $revision"
  else
    echo "Failed to register task definition"
    return 1
  fi
}

update_service() {
  # shellcheck disable=SC2039
  if [[ $(aws ecs update-service --cluster "$cluster" --service "$service" --task-definition "$revision" | $JQ '.service.taskDefinition') != "$revision" ]]; then
    echo "Error updating service."
    return 1
  fi
}

deploy_cluster() {

  cluster="origame"

  # origame
  service="origame-backend"
  template="ecs_origame_taskdefinition.json"
  task_template=$(cat "ecs/$template")
  # shellcheck disable=SC2059
  task_def=$(printf "$task_template" "$AWS_ACCOUNT_ID" "$AWS_RDS_URI" "$PRODUCTION_SECRET_KEY" "$DJANGO_ORIGAME_PORT")
  echo "$task_def"
  register_definition
  update_service

}

configure_aws_cli
deploy_cluster