from django.conf import settings
import telegram
import asyncio

def send_message(message, chat_id):
    bot = telegram.Bot(token=settings.TELEGRAM['token'])
    asyncio.run(bot.send_message(chat_id=f"{chat_id}",
                     text=message))
    
