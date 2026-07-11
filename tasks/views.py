from django.shortcuts import get_object_or_404, render, redirect

from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(
        request,
        "tasks/task_list.html",
        {"tasks": tasks},
    )


def task_detail(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
    )
    return render(
        request,
        "tasks/task_detail.html",
        {"task": task},
    )


def create_task(request):
    form = TaskForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        form.save()
        return redirect(
            "tasks:task_detail",
            pk=form.instance.pk,
        )

    return render(
        request,
        "tasks/create_task.html",
        context=context,
    )


def edit_task(request, pk):
    instance = get_object_or_404(Task, pk=pk)

    form = TaskForm(
        request.POST or None,
        instance=instance,
    )
    if form.is_valid():
        form.save()
        return redirect(
            "tasks:task_detail",
            pk=form.instance.pk,
        )

    return render(
        request,
        "tasks/edit_task.html",
        {"form": form},
    )


def delete_task(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        instance.delete()
        return redirect("tasks:task_list")
    return render(
        request,
        "tasks/delete_task.html",
        {"task": instance},
    )
