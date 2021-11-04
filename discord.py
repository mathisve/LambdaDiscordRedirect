import urllib3
import os
import json

BASE_URL = 'https://discordapp.com/api/v6'

WELCOME_CHANNEL_ID = os.environ.get("WELCOME_CHANNEL_ID")
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID")

BOT_TOKEN = os.environ.get("TOKEN")
INVITE_URL = "{}/channels/{}/invites".format(BASE_URL, WELCOME_CHANNEL_ID)
MESSAGE_URL = "{}/channels/{}/messages".format(BASE_URL, LOG_CHANNEL_ID)

http = urllib3.PoolManager()

headers = {
    'Authorization': 'Bot {}'.format(BOT_TOKEN),
    'Content-Type': 'application/json'
}

def create_invite(event):
    payload = {
        'max_age': 360,
        'max_uses': 1,
        'temporary': False,
        'unique': True
    }

    r = http.request("POST",
        INVITE_URL, 
        headers=headers, 
        body=json.dumps(payload),
    )

    if r.status == 429:
        return False, "<h1> try again later </h1>"
        print(r.status)
    
    if r.status == 200:
        c = json.loads(r.data.decode('utf-8'))
        send_message(event, c['code'])

        return True, 'https://discord.gg/{}'.format(c['code'])
    else:
        print("something went wrong when requesting invite: ", r.status)
        return False, "<h1> something went wrong! please let me know: mathis.vaneetvelde@protonmail.com </h1>"
        

def send_message(event, code):
    payload = {
        'content': 'Created Invite: `{}` for IP: `{}` User-Agent: `{}`'.format(code, event["requestContext"]["http"]["sourceIp"], event["headers"]["user-agent"]),
    }

    r = http.request("POST",
        MESSAGE_URL,
        headers=headers,
        body=json.dumps(payload),
    )

    if r.status != 200:
        print("something went wrong when sending message: ", r.status)
