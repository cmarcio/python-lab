#!/bin/sh

sqsEndpoint=http://localhost:4576

printf 'Using SQS endpoint: %s\n' $sqsEndpoint

createSQSQueue() {
    printf 'Creating Queue: %s\n' $1
    aws --endpoint-url=$sqsEndpoint sqs create-queue --queue-name $1 --region us-east-1
}

createSQSQueue test-queue
