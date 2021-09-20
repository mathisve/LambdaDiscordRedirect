import os
import urllib3
import json


BASE_URL = 'https://discordapp.com/api/v6'
CHANNEL_ID = os.environ.get("CHANNEL_ID")
BOT_TOKEN = os.environ.get("TOKEN")
URL = "{}/channels/{}/invites".format(BASE_URL, CHANNEL_ID)

http = urllib3.PoolManager()

def create_invite():
    headers = {
        'Authorization': 'Bot {}'.format(BOT_TOKEN),
        'Content-Type': 'application/json'
    }

    payload = {
        'max_age': 60,
        'max_uses': 1,
        'temporary': True,
        'unique': True
    }

    r = http.request("POST",
        URL, 
        headers=headers, 
        body=json.dumps(payload),
    )

   
    if r.status == 429:
        return False, "<h1> try again later </h1>"
    
    if r.status == 200:
        c = json.loads(r.data.decode('utf-8'))
        return True, 'https://discord.gg/{}'.format(c['code'])
    else:
        return False, "<h1> something went wrong! please let me know: mathis.vaneetvelde@protonmail.com </h1>"   

def lambda_handler(event, context):
    ok, invite = create_invite()
    
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