from django.core.management.base import BaseCommand, CommandError
from django_telegram_bot.telegram import start_bot
from django.conf import settings


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        try:
            settings.TELEGRAM['bot_name']
            settings.TELEGRAM['token']
        except:
            raise CommandError("TELEGRAM 'bot_name' or 'token' not found in settings file")
        self.stdout.write(self.style.SUCCESS('Starting %s' % settings.TELEGRAM['bot_name']))
        start_bot()