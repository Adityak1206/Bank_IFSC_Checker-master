from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

## Init Flask APp
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
  ## GEt user message
    user_msg = request.values.get('Body', '').lower()
    ## Init bot response
    bot_resp= MessagingResponse()
    msg = bot_resp.message()
    # Applying bot logic
    if 'hello' in user_msg:
        msg.body("Hi there! How may I help you?")
    elif 'check' in user_msg:
        r = requests.get('https://ifsc.razorpay.com/UTIB0003655')
        msg.body(r)
    else:
        msg.body("Sorry, I didn't get what you have said!")
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)