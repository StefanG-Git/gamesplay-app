from django.shortcuts import render, redirect

from gamesplay_app.main.models import Game
from gamesplay_app.profile_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from gamesplay_app.profile_app.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]

    return None


def profile_action(request, form_class, success_url_name, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url_name)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
    }

    return render(request, template_name, context)


def create_profile(request):
    return profile_action(request, CreateProfileForm, 'index', Profile(), 'profile/create-profile.html')


def show_profile_details(request):
    profile = get_profile()
    all_games = Game.objects.all()
    total_games_count = len(all_games)

    if total_games_count > 0:
        average_games_rating = sum(g.rating for g in all_games) / total_games_count
    else:
        average_games_rating = 0.0

    context = {
        'profile': profile,
        'total_games_count': total_games_count,
        'average_games_rating': average_games_rating,
    }

    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'show profile details', get_profile(), 'profile/edit-profile.html')


def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'profile/delete-profile.html')
