from django.views.generic import FormView, DetailView, ListView, DeleteView
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from users import mixins as user_mixins
from users import models as user_models
from . import models, forms


def toDoList(request):
    current_user = request.user
    all_todo = models.ToDoList.objects.all()
    indi_todo = []
    indi_todo_pk = []
    for todo in all_todo:
        if todo.host.id == current_user.id:
            indi_todo.append(todo.toDo)

    for todo in all_todo:
        if todo.host.id == current_user.id:
            indi_todo_pk.append(todo.pk)

    return render(request, "todo/todo_list.html", context={"todos": indi_todo, "todo_pk": indi_todo_pk, "user": current_user})


class CreateToDoView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateToDoForm
    template_name = "todo/todo_create.html"

    def form_valid(self, form):
        todo = form.save()
        todo.host = self.request.user
        todo.save()
        messages.success(self.request, "To Do Created")
        return redirect(reverse("todo:list"))


@login_required
def delete_todo(request):
    request_id = request.GET.get("id")
    todo = models.ToDoList.objects.get(id=request_id)
    todo.delete()
    messages.success(request, "To Do Deleted")
    return redirect(reverse("todo:list"))
