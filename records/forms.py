from django import forms
from . import models


class CreateToDoForm(forms.ModelForm):
    class Meta:
        model = models.ToDoList
        fields = (
            "toDo",
        )

    def save(self, *args, **kwargs):
        todo = super().save(commit=False)
        return todo
