from django.shortcuts import render

from gamesplay_app.main.models import Game


def show_home(request):
    return render(request, 'main/home-page.html')


def show_dashboard(request):
    games = Game.objects.all()
    context = {
        'games': games
    }

    return render(request, 'main/dashboard.html', context)


def create_game(request):
    pass


def show_game_details(request):
    pass


def edit_game(request):
    pass


def delete_game(request):
    pass
