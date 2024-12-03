__all__ = ()

import django.conf
import django.db.migrations
import django.db.models.deletion

import users.models


class Migration(django.db.migrations.Migration):

    initial = True

    dependencies = [
        django.db.migrations.swappable_dependency(
            django.conf.settings.AUTH_USER_MODEL,
        ),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        django.db.migrations.CreateModel(
            name="User",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth.user",),
            managers=[
                ("objects", users.models.UserManager()),
            ],
        ),
        django.db.migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    django.db.models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "birthday",
                    django.db.models.DateField(
                        blank=True,
                        help_text="Введите дату рождения",
                        null=True,
                        verbose_name="день рождения",
                    ),
                ),
                (
                    "image",
                    django.db.models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="uploads/profile",
                    ),
                ),
                (
                    "attempts_count",
                    django.db.models.PositiveIntegerField(default=0),
                ),
                (
                    "description",
                    django.db.models.TextField(blank=True, null=True),
                ),
                (
                    "date_last_active",
                    django.db.models.DateTimeField(blank=True, null=True),
                ),
                (
                    "user",
                    django.db.models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=django.conf.settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "дополнительная информация",
                "verbose_name_plural": "дополнительные данные",
            },
        ),
    ]
