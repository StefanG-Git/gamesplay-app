from django import forms

from gamesplay_app.profile_app.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'email': forms.TextInput(),
            'age': forms.NumberInput(),
            'password': forms.PasswordInput(),
        }
