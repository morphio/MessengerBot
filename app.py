import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':

        token_sent = request.args["hub.verify_token"]
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        sent_message(recipient_id, response_sent_text)
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
        return "Message Processed"

def send_message(recipient_id, response):

    bot.send_text-message(recipient_id, response)
    return "success"

def get_message():
    sample_responses = ["Потрясающе", "Я вами горжусь", "Продолжайте в том же духе"]
    return random.choice(sample_responses)
if __name__ == '__main__':
    app.run()
