import json
import boto3
import os

# reading SECRET from an environment variable
SECRET = os.environ['SECRET']

# ---------------------------------------------------------------
# Validates if the secret in the request is matching the expected secret
def validate_secret(event,secret):
    # getting the value of SECRET from the request URL
    secret_from_request = None
    try:
        secret_from_request = event['queryStringParameters']['SECRET']
    except Exception as e:
        print('ERROR: Secret is missing in the request. Exception: {}'.format(e))
        return False

    if secret_from_request != SECRET:
        print('ERROR: Secret in the request doesn\'t match the secret')
        return False
    else:
        return True

# ---------------------------------------------------------------
# Extracts data passed by IFTTT into an object
def get_body_from_event(event):
    body = None
    if 'body' in event:
        try:
            # need to use strict=False to allow for line breaks
            body = json.loads(event['body'], strict=False)
        except Exception as e:
            print('ERROR: Body is not valid JSON. Exception: {}'.format(e))
            return None
    else:
        print('ERROR: Body is missing in the event')
        return None

    return body

# ---------------------------------------------------------------
# The main Lambda handler function
def lambda_handler(event, context):
    # validating if SECRET is present in the request and valid
    if not validate_secret(event,SECRET):
        raise Exception('Secret is missing or invalid')

    # getting body from the event and raising an exception if it's missing
    body = get_body_from_event(event)
    if body == None:
        raise Exception('Body is missing or malformed')

    # ---------------------- #
    # Your code goes here    #
    # ---------------------- #
    print('body=')
    print('{}',json.dumps(body))

    return {"statusCode": 200}