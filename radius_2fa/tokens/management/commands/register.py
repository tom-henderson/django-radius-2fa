from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from tokens.models import Token

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
        user_model = get_user_model()
        user = user_model.objects.get(username=options['user']) # TODO: get or create?

        token = Token(user=user)
        token.save()

        qrcode_terminal.draw(token.qr)
