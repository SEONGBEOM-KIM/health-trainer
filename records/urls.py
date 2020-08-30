from django.urls import path
from . import views

app_name = "toDo"

urlpatterns = [
    path("list/", views.toDoList, name="list"),
    path("create/", views.CreateToDoView.as_view(), name="create"),
    path("delete/", views.delete_todo, name="delete"),
]
