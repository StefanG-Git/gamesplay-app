from django.urls import path

from gamesplay_app.profile_app.views import create_profile, show_profile_details, edit_profile, delete_profile

urlpatterns = (
    path('profile/create', create_profile, name='create profile'),
    path('profile/details/', show_profile_details, name='show profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
