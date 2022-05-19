from django import forms

from gamesplay_app.main.models import Game
from gamesplay_app.profile_app.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.TextInput(
                attrs={
                    'type': 'password'
                },
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Game.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
