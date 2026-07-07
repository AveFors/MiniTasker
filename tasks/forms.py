from django import forms

from .models import Task


class TaskForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label="Задача",
    )
    description = forms.CharField(
        label="Описание",
        required=False,
        widget=forms.Textarea,
    )
    status = forms.ChoiceField(
        choices=Task.STATUS_CHOICES,
        label="Статус",
    )
    deadline = forms.DateField(
        label="Дедлайн",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
    )
