import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('euVPgxXliNZadNBwabW+fNZW7OCLuz0TgbTfMH/2b3TQJF1WbzAth2FV29er+Sgmq5R9J8trRxsYLEG9fSXD7b3lvtDzw1OcnXeLfdSdWmGWlEjMtH3fO6x+9rzQsJ7ip78X+yNU3NQyxasOXrVkagdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b253e3857856e3501baa15be1a6a9df1')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

git commit -a -m "euVPgxXliNZadNBwabW+fNZW7OCLuz0TgbTfMH/2b3TQJF1WbzAth2FV29er+Sgmq5R9J8trRxsYLEG9fSXD7b3lvtDzw1OcnXeLfdSdWmGWlEjMtH3fO6x+9rzQsJ7ip78X+yNU3NQyxasOXrVkagdB04t89/1O/w1cDnyilFU="
heroku create
git push heroku master
