
from django_telegram_bot.serializers import SendTelegramSerializer, LinkTelegramSerializer
from django_telegram_bot.models import TelegramUser
from django_telegram_bot.utils import send_message
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

@api_view(['POST',])
def link_to_telegram(request):
    serializer = LinkTelegramSerializer(data = request.data)
    if not serializer.is_valid():
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    telegramUser = serializer.save()
    return Response({"Response": f"One more step! Start {settings.TELEGRAM['bot_name']} from your registered alias."},status=status.HTTP_201_CREATED)

@api_view(['POST',])
def send_to_telegram(request):
    serializer = SendTelegramSerializer(data = request.data)
    if not serializer.is_valid():
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.get(username = serializer.validated_data['username'])
        telegramUser = TelegramUser.objects.get(user=user)
        # check if user started the bot
        if telegramUser.chat_id == None:
            return Response({"Response": f"One more step! Start {settings.TELEGRAM['bot_name']} from your registered alias."},
                            status=status.HTTP_201_CREATED)
        
        message = f"Django says hello! Your username is {telegramUser.user.username}"
        # send message to user
        send_message(message,telegramUser.chat_id)
        return Response({"Response": f"Message sent to {telegramUser.alias}."},status=status.HTTP_200_OK)
    except Exception:
        return Response({"Error":"User does not have linked telegram account"},status=status.HTTP_400_BAD_REQUEST)
