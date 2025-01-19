from django.db import models
class Participant(models.Model):
    participant_id = models.AutoField(primary_key=True)  # Unique ID
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    nationality = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    affiliated_institution = models.CharField(max_length=255, blank=True, null=True)
    years_of_experience_in_neurology = models.IntegerField()
    expert_in_task_specific_dystonia = models.BooleanField(default=False)
    treated_task_specific_dystonia = models.BooleanField(default=False)
    primary_area_of_research = models.CharField(max_length=255)
    country_of_medical_training = models.CharField(max_length=255)
    further_comments = models.TextField(blank=True, null=True)
    consent_timestamp = models.DateTimeField(auto_now_add=True)  # When consent was given
    updated_at = models.DateTimeField(auto_now=True)
    video_order = models.JSONField(default=list)  # Stores randomized video order
    video_progress = models.IntegerField(default=0)  # Index of the last-seen video

    # New fields
    participant_number = models.CharField(max_length=10, unique=True, null=True, blank=True)  # To match Participation
    participation = models.OneToOneField(
        "Participation", on_delete=models.CASCADE, related_name="participant", null=True, blank=True
    )  # Link to Participation

    def __str__(self):
        return f"{self.participant_id} - {self.first_name} {self.last_name}"



from django.db import models
class Participation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    consent_given = models.BooleanField()
    consent_timestamp = models.DateTimeField(auto_now_add=True)
    completed_feedback = models.BooleanField(default=False)
    participant_number = models.CharField(max_length=10, unique=True, default='UNSPEC')


    def get_feedback_status(self):
        return "Yes" if self.completed_feedback else "No"

    get_feedback_status.short_description = "Feedback Completed"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Consent: {'Yes' if self.consent_given else 'No'}"



from django.db import models
class Feedback(models.Model):
    participant = models.ForeignKey('Participant', on_delete=models.CASCADE, null=True, blank=True)
    participant_number = models.CharField(max_length=10, null=True, blank=True)
    video_filename = models.CharField(max_length=255)
    rating = models.IntegerField()  # Rating or score
    yips_severity = models.IntegerField(null=True, blank=True)  # Likert scale 1–5
    neurological_disorder_present = models.BooleanField(null=True, blank=True)  # Binary Yes/No field
    comments = models.TextField(blank=True, null=True)  # Comments field
    feedback_timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp for feedback

    def save(self, *args, **kwargs):
        # Automatically populate participant_number from the linked Participant
        if self.participant and not self.participant_number:
            self.participant_number = self.participant.participant_number
        super().save(*args, **kwargs)

    def __str__(self):
        participant_info = (
            f"{self.participant_number or 'No Number'} - "
            f"{self.participant.first_name} {self.participant.last_name}" if self.participant else "Anonymous"
        )
        return f"{participant_info} - {self.video_filename} - Rating: {self.rating}"


###################################################


from django.contrib.auth.hashers import make_password

class UserAuth(models.Model):
    participant_number = models.CharField(max_length=10, unique=True)
    password_hash = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)

    def __str__(self):
        return f"UserAuth: {self.participant_number}"