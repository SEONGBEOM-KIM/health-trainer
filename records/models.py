from django.db import models
from django.shortcuts import reverse
from users import models as user_models


class ToDoList(models.Model):

    host = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, related_name="todolists")
    toDo = models.CharField(max_length=200, blank=True, null=True)

    # def get_absolute_url(self):
    #     return reverse("todo:list", kwargs={"pk": self.pk})
