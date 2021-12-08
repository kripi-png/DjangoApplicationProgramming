from django import forms

from .models import BoardGame, Review

class BoardGameForm(forms.ModelForm):

    class Meta:
        model = BoardGame
        fields = ['name', 'information']
        labels = {'name': '', 'information':''}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'score']
        labels = {'text': '', 'score': 'Score:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
