from django.urls import path

from gamesplay_app.main.views import show_home, show_dashboard, create_game, show_game_details, edit_game, delete_game

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('game/create/', create_game, name='create game'),
    path('game/details/<int:pk>/', show_game_details, name='show game details'),
    path('game/edit/<int:pk>/', edit_game, name='edit game'),
    path('game/delete/<id>/', delete_game, name='delete game'),
)
