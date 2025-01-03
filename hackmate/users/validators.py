__all__ = ()

import datetime

import django.core.exceptions
import django.core.validators
import django.utils.timezone
import django.utils.translation


def validate_birthday(value):
    today = django.utils.timezone.now().date()
    oldest_allowed = today - datetime.timedelta(days=150 * 365)
    youngest_allowed = today - datetime.timedelta(days=14 * 365)
    if value > today:
        raise django.core.exceptions.ValidationError(
            django.utils.translation.gettext_lazy(
                "Укажите корректную дату рождения.",
            ),
        )

    if value < oldest_allowed:
        raise django.core.exceptions.ValidationError(
            django.utils.translation.gettext_lazy(
                "Укажите корректную дату рождения.",
            ),
        )

    if value > youngest_allowed:
        raise django.core.exceptions.ValidationError(
            django.utils.translation.gettext_lazy(
                "Для участия в хакатонах вам должно быть минимум 14 лет",
            ),
        )


class MaxLengthPasswordValidator:
    def __init__(self, max_length=128):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise django.core.exceptions.ValidationError(
                django.utils.translation.gettext_lazy(
                    "Пароль может содержать максимум %(max_length)d символов.",
                ),
                code="password_too_long",
                params={"max_length": self.max_length},
            )

    def get_help_text(self):
        return django.utils.translation.gettext_lazy(
            "Пароль может содержать максимум %(max_length)d символов."
            % {"max_length": self.max_length},
        )


def validate_social_network_url(value, site_type):
    expected_prefixes = {
        "facebook": "https://facebook.com/",
        "twitter": "https://x.com/",
        "instagram": "https://www.instagram.com/",
        "vk": "https://vk.com/",
        "gitlab": "https://gitlab",
        "github": "https://github.com/",
    }

    if not site_type:
        raise django.core.exceptions.ValidationError(
            django.utils.translation.gettext_lazy("Тип сайта не указан."),
        )

    if site_type not in expected_prefixes:
        raise django.core.exceptions.ValidationError(
            django.utils.translation.gettext_lazy(
                f"Неизвестный тип сайта: {site_type}.",
            ),
        )

    expected_prefix = expected_prefixes[site_type]

    if not value.startswith(expected_prefix):
        raise django.core.exceptions.ValidationError(
            django.utils.translation.gettext_lazy(
                f"Ссылка должна начинаться с '{expected_prefix}'. "
                f"Текущий: {value}",
            ),
        )

    try:
        django.core.validators.URLValidator()(value)
    except django.core.exceptions.ValidationError:
        raise django.core.exceptions.ValidationError(
            django.utils.translation.gettext_lazy(
                f"Некорректный URL: {value}",
            ),
        )
