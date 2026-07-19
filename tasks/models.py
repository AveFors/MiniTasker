from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


from core.models import BaseModel
from .validators import (
    validate_deadline_not_in_past,
    validate_title_only_whitespace,
)


class Task(BaseModel):
    STATUS_TODO = "todo"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_DONE = "done"

    STATUS_CHOICES = [
        (STATUS_TODO, "To do"),
        (STATUS_IN_PROGRESS, "In progress"),
        (STATUS_DONE, "Done"),
    ]

    title = models.CharField(
        max_length=200,
        validators=(
            validate_title_only_whitespace,
            MinLengthValidator(3),
        ),
        verbose_name="Заголовок",
    )
    description = models.TextField(
        blank=True,
        max_length=2000,
        verbose_name="Описание",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_TODO,
        verbose_name="Статус",
    )
    deadline = models.DateField(
        blank=True,
        null=True,
        validators=(validate_deadline_not_in_past,),
        verbose_name="Дедлайн",
    )

    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "Задачи"

    def clean(self):
        super().clean()

        if self.STATUS_DONE == self.status and not self.description.strip():
            raise ValidationError(
                {"description": "У выполненной задачи должно быть описание."}
            )

    def __str__(self):
        return self.title
