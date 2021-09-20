from discord import *

def lambda_handler(event, context):
    print("event: ",  event)
    print("context: ", context)
    
    ok, invite = create_invite(event)
    
    if ok == True:
        f = open("index.html", "r")
        content = f.read().format(invite)
    else:
        content = invite

    return {
        "statusCode": 200,
        "body": content,
        "headers": {
            'Content-Type': 'text/html',
        }
    }