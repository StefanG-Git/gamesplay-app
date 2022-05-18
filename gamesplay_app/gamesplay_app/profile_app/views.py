from django.shortcuts import render

from gamesplay_app.profile_app.forms import CreateProfileForm


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/home-page.html')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)


def show_profile_details(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass
