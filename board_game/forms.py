from django import forms

from .models import BoardGame, Review

class BoardGameForm(forms.ModelForm):

    class Meta:
        model = BoardGame
        fields = ['name', 'description', 'image']
        labels = {'name': '', 'description':'', 'image': ''}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'score']
        labels = {'text': '', 'score': 'Score:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
