from django.contrib import admin

from gamesplay_app.profile_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age')
