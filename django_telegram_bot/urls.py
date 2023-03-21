from django.urls import path
from django_telegram_bot.views import send_to_telegram, link_to_telegram


urlpatterns = [
    path('send_to_telegram/', send_to_telegram),
    path('link_to_telegram/', link_to_telegram),
]