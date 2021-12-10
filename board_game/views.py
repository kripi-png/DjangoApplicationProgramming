from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import BoardGame, Review
from .forms import BoardGameForm, ReviewForm

def index(request):
    """Home page for BoardGame"""
    return render(request, 'board_game/index.html')

@login_required
def games(request):
    """Display all games."""
    games = BoardGame.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'board_game/games.html', context)

@login_required
def game(request, game_id):
    """Show a single game and all its entries"""
    game = BoardGame.objects.get(id=game_id)
    reviews = game.review_set.order_by('-date_added')
    context = {'game': game, 'reviews': reviews}
    return render(request, 'board_game/game.html', context)

@login_required
def new_game(request):
    """Add a new game"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = BoardGameForm()
    else:
        # Post data submitted; process data
        form = BoardGameForm(request.POST, request.FILES)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = request.user
            new_game.save()
            return redirect('board_game:games')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'board_game/new_game.html', context)

@login_required
def new_review(request, game_id):
    """Add a new review for a particular game"""
    game = BoardGame.objects.get(id=game_id)

    if request.method != 'POST':
        # No data submitted; create a blank forms
        form = ReviewForm()
    else:
        # POST data submitted; process data
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.game = game
            new_review.save()
            return redirect('board_game:game', game_id=game_id)
    # Display a blank or invalid review
    context = {'game': game, 'form': form}
    return render(request, 'board_game/new_review.html', context)

@login_required
def edit_review(request, review_id):
    """Edit an existing review."""
    review = Review.objects.get(id=review_id)
    game = review.game

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = ReviewForm(instance=review)
    else:
        # Post data submitted; process data
        form = ReviewForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game:game', game_id=game.id)

    context = {'review': review, 'game': game, 'form': form}
    return render(request, 'board_game/edit_review.html', context)
