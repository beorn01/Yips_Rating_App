# Generated by Django 4.2.17 on 2024-12-27 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("feedback_backend_project", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Participation",
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
                ("consent_given", models.BooleanField()),
                ("consent_timestamp", models.DateTimeField(auto_now_add=True)),
                ("completed_feedback", models.BooleanField(default=False)),
                (
                    "participant",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="feedback_backend_project.participant",
                    ),
                ),
            ],
        ),
    ]
