from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
from django.conf import settings
from django_telegram_bot.models import TelegramUser
import asgiref

GREETING_MESSAGE = f"Welcome to {settings.TELEGRAM['bot_name']}!"

# To avoid django.core.exceptions.SynchronousOnlyOperation exeption run database queries in sync functions
# then call it using asgiref.sync.sync_to_async in async telegram functions.
def create_message(alias, chat_id):
    telegramUser = TelegramUser.objects.filter(alias=alias)
    if telegramUser.exists():
        telegramUser = telegramUser[0]
        user = telegramUser.user
        telegramUser.chat_id=chat_id
        telegramUser.save()
        return f"Account is linked to {user.username}"
    return GREETING_MESSAGE

async def startCommand(update, context):
    chat_id=update.effective_chat.id
    alias=update.effective_chat.username
    create = asgiref.sync.sync_to_async(create_message)
    message = await create(alias, chat_id)
    await context.bot.send_message(chat_id=chat_id, text=message)

async def messageHandler(update, context):
    chat_id=update.effective_chat.id
    alias=update.effective_chat.username
    create = asgiref.sync.sync_to_async(create_message)
    message = await create(alias, chat_id)
    await context.bot.send_message(chat_id=chat_id, text=message)

def start_bot():
    token = settings.TELEGRAM['token']
    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', startCommand)
    message_handler = MessageHandler(None,messageHandler)

    application.add_handler(start_handler)
    application.add_handler(message_handler)
    
    application.run_polling()