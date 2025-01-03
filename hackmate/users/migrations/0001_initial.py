__all__ = ()

import django.conf
import django.db
import django.db.models.deletion

import users.models
import users.validators


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
                        validators=[users.validators.validate_birthday],
                        verbose_name="день рождения",
                    ),
                ),
                (
                    "image",
                    django.db.models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=users.models.user_directory_path,
                    ),
                ),
                (
                    "attempts_count",
                    django.db.models.PositiveIntegerField(default=0),
                ),
                (
                    "description",
                    django.db.models.TextField(
                        blank=True,
                        help_text="Расскажите о себе",
                        null=True,
                        verbose_name="о себе",
                    ),
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
            name="ProfileLink",
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
                    "site_type",
                    django.db.models.CharField(
                        choices=[
                            ("facebook", "Facebook"),
                            ("twitter", "Twitter"),
                            ("instagram", "Instagram"),
                            ("vk", "VK"),
                            ("gitlub", "GitLub"),
                            ("github", "GitHub"),
                        ],
                        max_length=20,
                        verbose_name="тип сайта",
                    ),
                ),
                (
                    "url",
                    django.db.models.URLField(
                        blank=True,
                        help_text=(
                            "Полная ссылка, например, https://example.com"
                        ),
                        null=True,
                        verbose_name="URL",
                    ),
                ),
                (
                    "profile",
                    django.db.models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="users.profile",
                        verbose_name="профиль",
                    ),
                ),
            ],
            options={
                "verbose_name": "ссылка",
                "verbose_name_plural": "ссылки",
            },
        ),
    ]
