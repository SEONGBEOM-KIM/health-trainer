import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command create Users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users do you want to create")

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {
            "is_staff": False,
            "is_superuser": False,
            "number": lambda x: random.randint(1, 50),
            "age": lambda x: random.randint(1, 100)
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} users Created!"))
