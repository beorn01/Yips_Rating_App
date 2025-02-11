# Generated by Django 4.2.17 on 2024-12-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "feedback_backend_project",
            "0006_rename_name_participant_first_name_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("video_filename", models.CharField(max_length=255)),
                ("rating", models.IntegerField()),
                ("comments", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="participant",
            name="affiliated_institution",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="participant",
            name="expert_in_task_specific_dystonia",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="participant",
            name="treated_task_specific_dystonia",
            field=models.BooleanField(default=False),
        ),
    ]
