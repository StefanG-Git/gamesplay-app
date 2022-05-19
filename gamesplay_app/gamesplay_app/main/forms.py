from django import forms

from gamesplay_app.main.models import Game


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = '__all__'
