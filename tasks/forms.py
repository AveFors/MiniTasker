from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "deadline", "status")
        widgets = {
            "deadline": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"},
            ),
            "description": forms.Textarea(),
        }
