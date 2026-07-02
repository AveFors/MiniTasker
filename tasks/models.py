from django.db import models
from core.models import BaseModel


class Task(BaseModel):
    STATUS_TODO = "todo"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_DONE = "done"

    STATUS_CHOICES = [
        (STATUS_TODO, "To do"),
        (STATUS_IN_PROGRESS, "In progress"),
        (STATUS_DONE, "Done"),
    ]

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_TODO,
        verbose_name="Статус",
    )
    deadline = models.DateField(blank=True, null=True, verbose_name="Дедлайн")

    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
