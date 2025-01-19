from django.contrib import admin
from .models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('participant_id', 'first_name', 'last_name', 'email', 'consent_timestamp')

admin.site.register(Participant, ParticipantAdmin)



from django.contrib import admin
from .models import Participation
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'consent_given', 'consent_timestamp', 'get_feedback_status')

    @admin.display(description="Feedback Completed")
    def get_feedback_status(self, obj):
        return "Yes" if obj.completed_feedback else "No"
# Register the Participation model with the custom admin class
admin.site.register(Participation, ParticipationAdmin)



from django.contrib import admin
from .models import Feedback

from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'participant',
        'video_filename',
        'rating',
        'yips_severity',
        'neurological_disorder_present',
        'feedback_timestamp'
    )
    search_fields = ('participant__name', 'video_filename', 'rating', 'comments')


##########################################

from .models import UserAuth

@admin.register(UserAuth)
class UserAuthAdmin(admin.ModelAdmin):
    list_display = ('participant_number',)


###################

