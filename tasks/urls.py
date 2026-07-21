from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("create/", views.TaskCreateView.as_view(), name="create_task"),
    path("edit/<int:pk>/", views.TaskUpdateView.as_view(), name="edit_task"),
    path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="delete_task"),
]
