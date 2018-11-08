# replace placeholder values with real values
export SECRET=CREATE_A_LONG_STRING_WITH_UUIDGEN_OR_SIMILAR
export S3_BUCKET=NAME_OF_S3_BUCKET_TO_PUBLISH_YOUR_CODE_TO
export STACK_NAME=NAME_OF_THE_STACK

# create bucket
aws s3 mb s3://${S3_BUCKET}

# package
sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket ${S3_BUCKET}

# deploy
sam deploy \
    --template-file packaged.yaml \
    --stack-name ${STACK_NAME} \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides Secret="${SECRET}"

# describe outputs
aws cloudformation describe-stacks \
    --stack-name ${STACK_NAME} \
    --query 'Stacks[].Outputs'