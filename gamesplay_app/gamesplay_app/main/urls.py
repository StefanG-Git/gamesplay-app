from django.urls import path

from gamesplay_app.main.views.games import create_game, delete_game, edit_game, show_game_details
from gamesplay_app.main.views.generic import show_home, show_dashboard

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('game/create/', create_game, name='create game'),
    path('game/details/<int:pk>/', show_game_details, name='show game details'),
    path('game/edit/<int:pk>/', edit_game, name='edit game'),
    path('game/delete/<int:pk>/', delete_game, name='delete game'),
)
