from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Task


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")

    return render(
        request,
        "dashboard.html",
        {"tasks": tasks}
    )


@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        status = request.POST.get("status", "pending")

        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                description=description,
                status=status
            )

            return redirect("dashboard")

    return render(request, "add_task.html")


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    if request.method == "POST":
        task.title = request.POST.get("title", "").strip()
        task.description = request.POST.get("description", "").strip()
        task.status = request.POST.get("status", "pending")

        if task.title:
            task.save()
            return redirect("dashboard")

    return render(
        request,
        "edit_task.html",
        {"task": task}
    )


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    if request.method == "POST":
        task.delete()
        return redirect("dashboard")

    return render(
        request,
        "delete_task.html",
        {"task": task}
    )