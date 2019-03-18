from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from tokens.models import Token
from datetime import datetime

import qrcode_terminal

class Command(BaseCommand):
    def log_message(self, message):
        self.stdout.write(
            u"[{}] {}".format(
                datetime.now(),
                message,
            )
        )

    def add_arguments(self, parser):
        parser.add_argument('user')

    def handle(self, **options):
        username = options['user']
        user_model = get_user_model()

        try:
            user = user_model.objects.get(username=username)
        except user_model.DoesNotExist:
            self.log_message(f"User {username} not found.")
            return False

        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            self.log_message(f"User {username} has no token to deregister.")
            return False

        token.delete()
        self.log_message(f"Token for user {username} has been deregistered.")
