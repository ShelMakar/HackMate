# Generated by Django 4.2 on 2024-12-15 19:02
__all__ = ()

import django.db.migrations


class Migration(django.db.migrations.Migration):

    dependencies = [
        ("star_ratings", "0004_alter_rating_id_alter_userrating_id"),
        ("users", "0001_initial"),
    ]

    operations = [
        django.db.migrations.CreateModel(
            name="CustomRating",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("star_ratings.rating",),
        ),
    ]
