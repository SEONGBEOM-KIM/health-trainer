from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "school",
                    "grade",
                    "group",
                    "number",
                    "gender",
                    "age",
                    "bio",
                    "login_method",
                )
            },
        ),
        (
            "PAPS Events",
            {
                "fields": (
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
                    "fat",
                )
            },
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "school",
        "grade",
        "group",
        "number",
        "gender",
        "age",
        "email_verified",
        "email_secret",
        "login_method",
    )

    list_filter = (
        "school",
        "gender",
        "grade",
    )

    search_fields = (
        "name",
        "school",
    )
