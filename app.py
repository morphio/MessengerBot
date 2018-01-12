from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET'

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
    
if __name__ == '__main__':
    app.run()
