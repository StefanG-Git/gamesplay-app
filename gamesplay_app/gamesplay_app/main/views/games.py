from django.shortcuts import render, redirect

from gamesplay_app.main.forms import CreateGameForm, EditGameForm, DeleteGameForm
from gamesplay_app.main.models import Game


def game_action(request, form_class, success_url_name, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url_name)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
        'game': instance,
    }

    return render(request, template_name, context)


def create_game(request):
    return game_action(request, CreateGameForm, 'dashboard', Game(), 'main/create-game.html')


def show_game_details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
    }

    return render(request, 'main/details-game.html', context)


def edit_game(request, pk):
    return game_action(request, EditGameForm, 'dashboard', Game.objects.get(pk=pk), 'main/edit-game.html')


def delete_game(request, pk):
    return game_action(request, DeleteGameForm, 'dashboard', Game.objects.get(pk=pk), 'main/delete-game.html')
