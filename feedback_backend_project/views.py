from django.shortcuts import render, redirect
from .models import Participation, Participant

from .models import Participation
from django.shortcuts import render, redirect
from django.contrib import messages
def informed_consent(request, participant_number):
    if request.method == "POST":
        # Collect form data
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        consent = request.POST.get("consent") == "yes"

        # Validate input
        if not first_name or not last_name:
            messages.error(request, "First name and last name are required.")
            return render(request, "informed_consent.html", {"participant_number": participant_number})

        # Create a Participation record
        participation = Participation.objects.create(
            first_name=first_name,
            last_name=last_name,
            consent_given=consent,
            participant_number=participant_number
        )

        # Redirect based on consent
        if consent:
            return redirect("register_participant", participation_id=participation.id)
        else:
            return render(request, "thank_you.html")

    return render(request, "informed_consent.html", {"participant_number": participant_number})


def register_participant(request, participation_id):
    if request.method == 'POST':
        # Collect participant details from the form
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'nationality': request.POST.get('nationality'),
            'specialty': request.POST.get('specialty'),
            'affiliated_institution': request.POST.get('affiliated_institution'),
            'years_of_experience_in_neurology': request.POST.get('years_of_experience_in_neurology'),
            'expert_in_task_specific_dystonia': request.POST.get('expert_in_task_specific_dystonia') == 'on',
            'treated_task_specific_dystonia': request.POST.get('treated_task_specific_dystonia') == 'on',
            'primary_area_of_research': request.POST.get('primary_area_of_research'),
            'country_of_medical_training': request.POST.get('country_of_medical_training'),
            'further_comments': request.POST.get('further_comments'),
        }

        # Retrieve the Participation record
        participation = Participation.objects.get(id=participation_id)

        # Check if a Participant already exists for this participation_number
        participant, created = Participant.objects.get_or_create(
            participant_number=participation.participant_number,
            defaults={
                **data,
                'participation': participation,  # Link to Participation model
                'consent_timestamp': participation.consent_timestamp
            }
        )

        # If the Participant already exists, update their details
        if not created:
            for field, value in data.items():
                setattr(participant, field, value)
            participant.save()

        # Store participant_number in session
        request.session["participant_number"] = participant.participant_number

        # Redirect to video feedback or completion page
        return redirect('show_video')  # Placeholder for next step

    # Pass participation details to pre-fill the form
    participation = Participation.objects.get(id=participation_id)
    context = {
        'first_name': participation.first_name,
        'last_name': participation.last_name,
    }
    return render(request, 'register_participant.html', context)



from django.shortcuts import render, redirect
from .models import Feedback
from .utils import generate_presigned_url, list_videos_in_bucket
def show_video(request):
    participant_number = request.session.get("participant_number")
    if not participant_number:
        return HttpResponse("Participant not found", status=400)

    participant = Participant.objects.get(participant_number=participant_number)
    video_list = participant.video_order
    video_progress = participant.video_progress

    if video_progress >= len(video_list):
        return render(request, "completion.html")  # Redirect to completion page

    current_video = video_list[video_progress]
    video_url = generate_presigned_url(current_video)

    context = {
        "video_url": video_url,
        "video_filename": current_video,
        "progress": f"{video_progress + 1} of {len(video_list)}",
    }

    return render(request, "show_video.html", context)


from .models import Participant
def submit_feedback(request):
    if request.method == "POST":
        video_filename = request.POST["video_filename"]
        rating = int(request.POST["rating"])
        yips_severity = int(request.POST["yips_severity"])
        neurological_disorder_present = request.POST["neurological_disorder_present"] == "yes"
        comments = request.POST.get("comments", "")

        participant_number = request.session.get("participant_number")

        # Graceful handling of missing participants
        try:
            participant = Participant.objects.get(participant_number=participant_number)
        except Participant.DoesNotExist:
            return HttpResponse("Participant not found", status=400)

        # Save feedback
        Feedback.objects.create(
            participant=participant,
            video_filename=video_filename,
            rating=rating,
            yips_severity=yips_severity,
            neurological_disorder_present=neurological_disorder_present,
            comments=comments
        )

        # Increment video progress
        participant.video_progress += 1
        participant.save()

        return redirect("show_video")



###############################################



from .models import UserAuth, Participation
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import generate_unique_participant_number, generate_random_password

import os  # To access environment variables
from django.contrib.auth.hashers import make_password

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import UserAuth, Participation
from .utils import generate_unique_participant_number
import os

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from .models import UserAuth

def user_authentication(request):
    """
    Unified entry point for new and existing user actions.
    Redirects based on user selection.
    """
    if request.method == "POST":
        action = request.POST.get("action")
        
        if action == "new_user":
            # Redirect to new user credentials flow
            return redirect("new_user_credentials")
        
        elif action == "existing_user":
            # Redirect to existing user login page
            return redirect("authenticate_existing_user")
        
        else:
            # Handle unexpected action inputs
            return render(request, "user_authentication.html", {
                "error_message": "Invalid selection. Please try again."
            })
    
    # Render the authentication form by default
    return render(request, "user_authentication.html")



from .models import Participant, UserAuth
from .utils import list_videos_in_bucket, generate_unique_participant_number
import random
import os
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

def new_user_credentials(request):
    if request.method == "GET":
        request.session.flush()  # Clear session data to avoid stale values

        # Generate a participant number
        participant_number = generate_unique_participant_number()

        # Temporarily store the participant number in the session
        request.session["participant_number"] = participant_number

    else:
        # Retrieve the participant number from the session
        participant_number = request.session.get("participant_number")

    if request.method == "POST":
        submitted_password = request.POST.get("password")
        fixed_password = os.getenv("FIXED_USER_PASSWORD")

        if submitted_password == fixed_password:
            # Fetch and randomize video list
            video_list = list_videos_in_bucket()
            random.shuffle(video_list)

            # Save the participant to the database
            participant = Participant.objects.create(
                participant_number=participant_number,
                video_order=video_list,
                years_of_experience_in_neurology=0,
                first_name="",
                last_name="",
                email=""
            )

            # Save the user credentials in UserAuth
            UserAuth.objects.create(
                participant_number=participant_number,
                password_hash=make_password(fixed_password)
            )

            # Redirect to participant number creation
            return redirect("participant_number_creation", participant_number=participant_number)
        else:
            return HttpResponse("Incorrect password. Please try again.", status=403)

    # Pass the participant number to the template
    return render(request, "new_user_credentials.html", {"participant_number": participant_number})





# Participant Number Creation (Renamed from the original logic)
def participant_number_creation(request, participant_number):
    return redirect("informed_consent", participant_number=participant_number)


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from .models import UserAuth, Participant

def existing_user_login(request):
    if request.method == "GET":
        # Fetch all participant numbers
        participants = Participant.objects.values("participant_number")
        return render(request, "existing_user_login.html", {"participants": participants})

    elif request.method == "POST":
        participant_number = request.POST.get("participant_number")
        password = request.POST.get("password")

        try:
            user = UserAuth.objects.get(participant_number=participant_number)
        except UserAuth.DoesNotExist:
            return render(request, "existing_user_login.html", {"error_message": "Invalid participant number."})

        if check_password(password, user.password_hash):
            # Store the participant number in the session
            request.session["participant_number"] = participant_number

            # Redirect to continue videos
            return redirect("show_video")
        else:
            return render(request, "existing_user_login.html", {"error_message": "Invalid password."})


from django.shortcuts import render, redirect
from django.contrib.auth import logout

def participant_logout(request):
    # Clear the session
    request.session.flush()
    return redirect("user_authentication")  # Redirect to the authentication page
