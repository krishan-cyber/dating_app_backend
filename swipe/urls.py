from django.urls import path
from .views import swipe_user,get_matches,fetch_profiles

urlpatterns = [
    path("swipe/", swipe_user, name="swipe-user"),
    path("matches/", get_matches, name="get-matches"),
    path("profiles/", fetch_profiles, name="fetch_profiles"),  
]