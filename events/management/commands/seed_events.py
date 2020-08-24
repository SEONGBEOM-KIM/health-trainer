from django.core.management.base import BaseCommand
from events import models as events_models


class Command(BaseCommand):

    help = "This command create Measurement Item"

    def add_arguments(self, parser):
        parser.add_argument("--times", help="")

    def handle(self, *args, **options):
        events = ["pacer", "ongTimeRun", "stepTest", "bendFoward", "totalFlexibility", "pushUp", "sitUp",
                  "grip", "sprint", "longJump", "height", "weight", "fat"]

        for event in events:
            events_models.MeasurementItem.objects.create(name=event)
        self.stdout.write(self.style.SUCCESS("Events Created!"))
