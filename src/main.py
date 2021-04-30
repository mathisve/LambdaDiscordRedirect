import os

f = open("index.html", "r")
content = f.read()
content = content.format(os.environ.get("INVITE"))

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": content,
        "headers": {
            'Content-Type': 'text/html',
        }
    }
