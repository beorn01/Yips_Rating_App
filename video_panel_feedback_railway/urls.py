"""
URL configuration for video_panel_feedback_railway project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect


def redirect_to_user_authentication(request):
    """Redirect to the user authentication page."""
    return HttpResponseRedirect("/user-authentication/")  # Redirect base URL to user authentication


urlpatterns = [
    path("admin/", admin.site.urls),  # Admin panel
    path("", redirect_to_user_authentication, name="redirect_to_user_authentication"),  # Redirect base URL to user authentication
    path("", include("feedback_backend_project.urls")),  # Include app-level URLs
]
