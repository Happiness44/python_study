import os
import telegram
from dotenv import load_dotenv

load_dotenv(verbose=True)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_USER_ID = os.getenv('CHAT_USER_ID')


bot = telegram.Bot(token=TELEGRAM_TOKEN)

#for i in bot.getUpdates():
#    print(i.message)

bot.sendMessage(chat_id=CHAT_USER_ID, text="테스트입니다.")


