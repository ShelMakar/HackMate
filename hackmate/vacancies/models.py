__all__ = ()

import django.conf
import django.core.validators
import django.db.models


class Ip(django.db.models.Model):
    ip = django.db.models.CharField(max_length=100)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "IP адрес"
        verbose_name_plural = "IP адреса"


class Vacancy(django.db.models.Model):
    class VacancyStatuses(django.db.models.TextChoices):
        ACTIVE = "active", "active"
        INACTIVE = "inactive", "inactive"

    creater = django.db.models.ForeignKey(
        django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.CASCADE,
        verbose_name="создатель вакансии",
    )

    title = django.db.models.CharField(
        max_length=255,
        verbose_name="название вакансии",
    )

    description = django.db.models.TextField(
        verbose_name="описание вакансии",
        validators=[
            django.core.validators.MinLengthValidator(
                5,
                "Описание не может быть таким коротким",
            ),
            django.core.validators.MaxLengthValidator(
                10000,
                "Описание не может быть таким длинным",
            ),
        ],
        help_text="Описание вакансии должно быть от 5 до 10000 символов",
    )

    created_at = django.db.models.DateTimeField(
        auto_now_add=True,
        verbose_name="создано",
    )

    updated_at = django.db.models.DateTimeField(
        auto_now=True,
        verbose_name="обновлено",
    )

    status = django.db.models.CharField(
        max_length=255,
        choices=VacancyStatuses.choices,
        verbose_name="cтатус",
    )

    views = django.db.models.ManyToManyField(
        Ip,
        related_name="post_views",
        blank=True,
    )

    hackaton_title = django.db.models.CharField(
        max_length=255,
        verbose_name="название хакатона",
        blank=True,
        null=True,
        help_text="Название хакатона, к которому относится вакансия",
    )

    deadline = django.db.models.DateField(
        verbose_name="дедлайн",
        null=True,
        blank=True,
        help_text="Крайний срок подачи заявок",
    )

    required_experience = django.db.models.IntegerField(
        verbose_name="требуемый опыт (в годах)",
        null=True,
        blank=True,
        help_text=(
            "Укажите количество лет опыта " "необходимого для кандидата"
        ),
        validators=[
            django.core.validators.MinValueValidator(
                0,
                "Введите корректное значение",
            ),
            django.core.validators.MaxValueValidator(
                100,
                "Введите корректное значение",
            ),
        ],
    )

    team_composition = django.db.models.ManyToManyField(
        django.conf.settings.AUTH_USER_MODEL,
        related_name="team_composition",
        verbose_name="состав команды",
    )

    class Meta:
        verbose_name = "вакансия"
        verbose_name_plural = "вакансии"
        ordering = ["-created_at"]

    def total_views(self):
        return self.views.count()

    def __str__(self):
        return self.title


class CommentVacancy(django.db.models.Model):
    vacancy = django.db.models.ForeignKey(
        "Vacancy",
        on_delete=django.db.models.CASCADE,
        verbose_name="вакансия",
        related_name="comments",
    )

    comment = django.db.models.TextField(
        verbose_name="комментарий",
        validators=[
            django.core.validators.MinLengthValidator(
                5,
                "Слишком короткий комментарий!",
            ),
            django.core.validators.MaxLengthValidator(
                3000,
                "Комментарий не может привышать 3000 символов!",
            ),
        ],
    )

    user = django.db.models.ForeignKey(
        django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.CASCADE,
        verbose_name="пользователь",
    )

    created_at = django.db.models.DateTimeField(
        auto_now_add=True,
        verbose_name="cоздано",
    )

    class Meta:
        verbose_name = "комментарий к вакансии"
        verbose_name_plural = "комментарии к вакансиям"
        ordering = ["-created_at"]


class Response(django.db.models.Model):
    class ResponseStatuses(django.db.models.TextChoices):
        ACCEPTED = "accepted", "accepted"
        REJECTED = "rejected", "rejected"
        NOT_ANSWERED = "not_answered", "not_answered"

    user = django.db.models.ForeignKey(
        django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.CASCADE,
        related_name="responses",
        verbose_name="пользователь",
        unique=False,
    )
    vacancy = django.db.models.ForeignKey(
        "Vacancy",
        on_delete=django.db.models.CASCADE,
        related_name="responses",
        verbose_name="вакансия",
        unique=False,
    )
    created_at = django.db.models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата отклика",
    )

    status = django.db.models.CharField(
        choices=ResponseStatuses.choices,
        max_length=255,
        default=ResponseStatuses.NOT_ANSWERED,
    )

    class Meta:
        verbose_name = "отклик"
        verbose_name_plural = "отклики"

    def __str__(self):
        return f"{self.user} -> {self.vacancy}"
