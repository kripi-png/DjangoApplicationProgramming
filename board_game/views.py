from django.shortcuts import render

from .models import BoardGame

def index(request):
    # Home page for BoardGame
    return render(request, 'board_game/index.html')

def games(request):
    """Display all games."""
    games = BoardGame.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'board_game/topics.html', context)
