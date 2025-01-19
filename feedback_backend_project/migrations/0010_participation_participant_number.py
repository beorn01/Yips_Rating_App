from django.db import migrations, models

def truncate_participant_number(apps, schema_editor):
    Participation = apps.get_model("feedback_backend_project", "Participation")
    for record in Participation.objects.all():
        record.participant_number = "UNKNOWN"  # Ensure the value fits within max_length=10
        record.save()

class Migration(migrations.Migration):
    dependencies = [
        ("feedback_backend_project", "0009_userauth"),
    ]

    operations = [
        migrations.AddField(
            model_name="participation",
            name="participant_number",
            field=models.CharField(max_length=10, unique=True, default="UNKNOWN"),
        ),
        migrations.RunPython(truncate_participant_number),
    ]
