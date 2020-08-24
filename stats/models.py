from django.db import models
from django.urls import reverse
from users import models as user_models


class Stats(models.Model):

    """ Stats Model Definition """

    name = models.ForeignKey(
        user_models.User, related_name="stats", on_delete=models.CASCADE
    )
    pacer = models.IntegerField(blank=True, null=True)
    longTimeRun = models.IntegerField(blank=True, null=True)
    stepTest = models.IntegerField(blank=True, null=True)
    bendFoward = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )
    totalFlexibility = models.IntegerField(blank=True, null=True)
    pushUp = models.IntegerField(blank=True, null=True)
    sitUp = models.IntegerField(blank=True, null=True)
    grip = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sprint = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    longJump = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True
    )
    height = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    fat = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return f"{self.name.name}({self.name.school})"

    def bmi(self):
        return round(self.weight / ((self.height / 100) ** 2), 2)

    class Meta:
        verbose_name_plural = "Stats"

    def get_absolute_url(self):
        return reverse("stats:detail", kwargs={"user_pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
