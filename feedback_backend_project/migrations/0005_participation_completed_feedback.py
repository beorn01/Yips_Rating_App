# Generated by Django 4.2.17 on 2024-12-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "feedback_backend_project",
            "0004_remove_participation_completed_feedback_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="participation",
            name="completed_feedback",
            field=models.BooleanField(default=False),
        ),
    ]
