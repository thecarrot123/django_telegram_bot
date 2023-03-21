from rest_framework import serializers
from django_telegram_bot.models import TelegramUser
from django.contrib.auth.models import User

class SendTelegramSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, required=True)

    def validate_username(self, value):
        try:
            User.objects.get( username = value )
            return value
        except:
            raise serializers.ValidationError("User Does Not Exist.")


class LinkTelegramSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=30, required=True)

    class Meta:
        model = TelegramUser
        fields = ['username','alias']

    def validate_username(self, value):
        try:
            User.objects.get( username = value )
            return value
        except:
            raise serializers.ValidationError("User Does Not Exist.")

    def save(self):
        telegramUser = TelegramUser(
            user = User.objects.get( username = self.validated_data['username'] ),
            alias = self.validated_data['alias'],
            chat_id = None,
        )
        telegramUser.save()
        return telegramUser