from datetime import date

from django.core.exceptions import ValidationError


def validate_deadline_not_in_past(value: date) -> None:
    today_date = date.today()

    if today_date > value:
        raise ValidationError("Дедлайн не может находиться в прошлом.")


def validate_title_only_whitespace(value: str) -> None:
    if not value.strip():
        raise ValidationError("Заголовок не может состоять только из пробелов")
