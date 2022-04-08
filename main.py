import telegram # pip install python-telegram-bot
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
TO_CHANNEL = os.environ.get("TO_CHANNEL", None)
START_MSG = os.environ.get("START_MSG", None)
STOP_MSG = os.environ.get("STOP_MSG", None)

TOKEN = "{BOT_TOKEN}"  # Replace telegram bot api token here
START_MSG = {START_MSG}  # Change value according your requirement
STOP_MSG = {STOP_MESSEGE}  # Change value according your requirement
DEST_ID = "{FROM_CHANNEL}"  # change with your Source Channal Username/ID
SRC_ID = "{TO_CHANNEL}"  # change with your Destination/Backup Channal Username/ID

auth = telegram.Bot(token=TOKEN)
def forward(START_MSG):
    try :
        for msg in range (START_MSG,STOP_MSG+1):
            telegram.Bot.forwardMessage(auth, chat_id=DEST_ID, from_chat_id=SRC_ID, message_id=msg)
    except telegram.error.BadRequest:
        START_MSG = msg+1
        forward(START_MSG)

if __name__ == "__main__":
    forward(START_MSG)
