from django.contrib import admin
from users import models as user_models
from . import models


@admin.register(models.Stats)
class StatsAdmin(admin.ModelAdmin):

    """ Stats Admin Definition """

    list_display = (
        "__str__",
        "pacer",
        "longTimeRun",
        "stepTest",
        "bendFoward",
        "totalFlexibility",
        "pushUp",
        "sitUp",
        "grip",
        "sprint",
        "longJump",
        "height",
        "weight",
        "bmi",
        "fat",
    )

    fieldsets = (
        ("Basic Info", {"fields": ("name",)}),
        ("Cardivascular Endurance", {"fields": ("pacer", "longTimeRun", "stepTest",)}),
        ("Flexibility", {"fields": ("bendFoward", "totalFlexibility",)}),
        (
            "Muscular Strength / Endurance",
            {"fields": ("pushUp", "sitUp", "grip", "sprint", "longJump",)},
        ),
        ("Body Fat Percentage", {"fields": ("height", "weight", "fat",)}),
    )

    search_fields = ("name__username", "name__school", "name__name")

    # def cal_bmi(self, obj):
    #     return round(obj.weight/((obj.height/100)**2), 2)

    # cal_bmi.short_description = "BMI"
