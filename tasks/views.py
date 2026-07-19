from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator

from .models import Task
from .forms import TaskForm

# TODO Сделать пагинацию + валидацию.


def task_list(request):
    tasks = Task.objects.order_by("-created_at")

    paginator = Paginator(tasks, 3)
    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "tasks/task_list.html",
        {"page_obj": page_obj},
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
