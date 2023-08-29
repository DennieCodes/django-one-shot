from django.shortcuts import render, get_object_or_404
from todos.models import TodoList


def todo_list_list(request):
    todo_list = TodoList.objects.all()

    context = {"todo_list_object": todo_list}

    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {"todo_list_object": todo_list}

    return render(request, "todos/detail.html", context)
