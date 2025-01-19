# Generated by Django 4.2.17 on 2024-12-28 17:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        (
            "feedback_backend_project",
            "0007_feedback_alter_participant_affiliated_institution_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="feedback_timestamp",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="feedback",
            name="participant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="feedback_backend_project.participant",
            ),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="comments",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="VideoFeedback",
        ),
    ]
