from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "created_at", "updated_at")
    list_filter = ("status", "deadline")
    search_fields = ("title", "description")


admin.site.register(Task, TaskAdmin)
