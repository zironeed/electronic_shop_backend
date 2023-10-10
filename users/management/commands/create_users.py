from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """A command for easily creating a user and superuser"""
    def handle(self, *args, **options):
        admin = User.objects.create(
            email='admin@gmail.com',
            first_name='admin',
            last_name='admin',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

        admin.set_password('12345')
        admin.save()

        user = User.objects.create(
            email='user@gmail.com',
            first_name='user',
            last_name='user',
            is_active=True,
            is_staff=True,
            is_superuser=False
        )

        user.set_password('12345')
        user.save()
