from django.shortcuts import render, redirect

from .models import BoardGame
from .forms import BoardGameForm

def index(request):
    # Home page for BoardGame
    return render(request, 'board_game/index.html')

def games(request):
    """Display all games."""
    games = BoardGame.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'board_game/games.html', context)

def game(request, game_id):
    """Show a single game and all its entries"""
    game = BoardGame.objects.get(id=game_id)
    reviews = game.review_set.order_by('-date_added')
    context = {'game': game, 'reviews': reviews}
    return render(request, 'board_game/game.html', context)

def new_game(request):
    """Add a new game"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = BoardGameForm()
    else:
        # Post data submitted; process data
        form = BoardGameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game:games')

        # Display a blank or invalid form
        context = {'form': form}
        return render(request, 'board_game/new_game.html', context)
