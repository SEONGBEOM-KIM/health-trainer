from django.shortcuts import render
from . import models


def exercise(request):
    return render(request, "exercise/exercise_main.html")


def squat(request):
    return render(request, "exercise/squat/squat_display.html")
