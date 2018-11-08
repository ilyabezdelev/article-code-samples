import json
import boto3
import os

SECRET = os.environ['SECRET']

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

def lambda_handler(event, context):
    # validating if SECRET is present in the request and valid
    if not validate_secret(event,SECRET):
        raise Exception('Secret invalid or missing')

    # getting body from the event
    body = get_body_from_event(event)

    if body == None:
        raise Exception('Body is missing or malformed')

    # ---------------------- #
    # Here goes your code    #
    # ---------------------- #
    print('body=')
    print('{}',json.dumps(body))

    return {"statusCode": 200}