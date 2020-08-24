from django.urls import path
from . import views

app_name = "exercise"

urlpatterns = [
    path("main/", views.exercise, name="main"),
    path("squat/", views.squat, name="squat"),
]
