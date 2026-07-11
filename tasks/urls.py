from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("<int:pk>/", views.task_detail, name="task_detail"),
    path("create/", views.create_task, name="create_task"),
    path("edit/<int:pk>/", views.edit_task, name="edit_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
]
