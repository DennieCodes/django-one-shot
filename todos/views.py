from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoListForm


# TODO_LIST_UPDATE
def todo_list_update(request, id):
    todo_list = get_object_or_404(TodoList, id=id)

    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=todo_list)

    context = {"todo_list": todo_list, "form": form}

    return render(request, "todos/update.html", context)


# TODO_LIST_CREATE
def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todolist = form.save()

            return redirect("todo_list_detail", id=todolist.id)
    else:
        form = TodoListForm()

    context = {"form": form}

    return render(request, "todos/create.html", context)


# TODO_LIST_LIST
def todo_list_list(request):
    todo_list = TodoList.objects.all()

    context = {"todo_list_object": todo_list}

    return render(request, "todos/list.html", context)


# TODO_LIST_DETAIL
def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {"todo_list_object": todo_list}

    return render(request, "todos/detail.html", context)
