# Generated by Django 4.1 on 2022-08-22 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("info_park_v2", "0002_alter_content_options_remove_content_pub_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mail", models.EmailField(max_length=100)),
                (
                    "content",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="info_park_v2.content",
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="account_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "password",
                    models.ForeignKey(
                        max_length=15,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="Myaccount",),
    ]
