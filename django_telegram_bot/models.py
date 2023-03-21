from django.db.models.deletion import CASCADE
from django.db import models
from django.conf import settings

class TelegramUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=CASCADE,primary_key=True,related_name="telegram_user")
    alias = models.CharField(max_length=35,unique=True)
    chat_id = models.CharField(max_length=35,default=None,null=True,blank=True)
