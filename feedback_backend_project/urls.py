from django.urls import path
from . import views

urlpatterns = [
    path("existing-user-login/", views.existing_user_login, name="authenticate_existing_user"),
    path('user-authentication/', views.user_authentication, name='user_authentication'),
    path('credentials/', views.new_user_credentials, name='new_user_credentials'),
    path("participant-number-creation/<str:participant_number>/", views.participant_number_creation, name="participant_number_creation"),
    path('consent/<str:participant_number>/', views.informed_consent, name='informed_consent'),
    path('register/<int:participation_id>/', views.register_participant, name='register_participant'),
    path('show_video/', views.show_video, name='show_video'),
    path("logout/", views.participant_logout, name="participant_logout"),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
]
