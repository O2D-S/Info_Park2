# Generated by Django 4.1 on 2022-08-22 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("info_park_v2", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(name="content", options={},),
        migrations.RemoveField(model_name="content", name="pub_date",),
        migrations.CreateModel(
            name="Myaccount",
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
                        related_name="myaccount_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
