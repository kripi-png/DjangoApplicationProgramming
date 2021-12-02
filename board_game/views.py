from django.shortcuts import render

def index(request):
    # Home page for BoardGame
    return render(request, 'board_game/index.html')
