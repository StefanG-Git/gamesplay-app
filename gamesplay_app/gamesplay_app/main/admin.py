from django.contrib import admin

from gamesplay_app.main.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'rating')
