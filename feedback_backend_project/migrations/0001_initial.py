# Generated by Django 4.2.17 on 2024-12-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Participant",
            fields=[
                ("participant_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("nationality", models.CharField(max_length=255)),
                ("specialty", models.CharField(max_length=255)),
                ("affiliated_institution", models.CharField(max_length=255)),
                ("years_of_experience_in_neurology", models.IntegerField()),
                ("expert_in_task_specific_dystonia", models.BooleanField()),
                ("treated_task_specific_dystonia", models.BooleanField()),
                ("primary_area_of_research", models.CharField(max_length=255)),
                ("country_of_medical_training", models.CharField(max_length=255)),
                ("further_comments", models.TextField(blank=True, null=True)),
                ("consent_timestamp", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
