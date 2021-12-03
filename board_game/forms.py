from django import forms

from .models import BoardGame, Review

from .models import BoardGame

class BoardGameForm(forms.ModelForm):

    class Meta:
        model = BoardGame
        fields = ['name']
        labels = {'name': ''}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'score']
        labels = {'text': '', 'score': 'Score:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
