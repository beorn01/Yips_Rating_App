# Generated by Django 4.2.17 on 2024-12-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feedback_backend_project", "0013_feedback_participant_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="participant",
            name="video_order",
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name="participant",
            name="video_progress",
            field=models.IntegerField(default=0),
        ),
    ]
