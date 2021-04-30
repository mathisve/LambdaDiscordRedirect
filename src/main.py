import random
import os

def lambda_handler(event, context):

    randomStrings = [
        "Discord Server",
        "Brain empty",
        "click me!",
        "Join us!",
        "./join.sh",
        "GOlang more like GOMAMA"]

    content = """
    <!DOCTYPE html>
        <html>
        <head>
            <meta name="og:description" content="{}">
            <meta name="og:title" content="Mathclass">
            <meta name="og:icon" content="https://media.discordapp.net/attachments/795655614856298536/798033310747983872/mathis.png?width=810&height=686">
            <meta name="og:url" content="https://discord.mathisvaneetvelde.com">
            <meta name="theme-color" content="#29beb0">

            <meta name="twitter:description" content="{}">
            <meta name="twitter:title" content="Mathclass">
            <meta name="twitter:image" content="https://media.discordapp.net/attachments/795655614856298536/798033310747983872/mathis.png?width=810&height=686">

            <meta http-equiv="refresh" content="0; url={}">
        </head>

        <body style="background-color: #2c2f33;">
        <h3> request data may be stored and used for further analysis </h3>
        </body>
    </html>
    """.format(random.choice(randomStrings), random.choice(randomStrings), os.environ.get("INVITE"))

    response = {
    "statusCode": 200,
    "body": content,
    "headers": {
        'Content-Type': 'text/html',
        }
    }

    return response