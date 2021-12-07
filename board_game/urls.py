# Define URL pattern for board_game

from django.urls import path

from . import views

app_name = 'board_game'

urlpatterns =[
    # Home page
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
    # Detail page for a single boardGame
    path('games/<int:game_id>/', views.game, name='game'),
    # Page for adding a new game
    path('new_game/', views.new_game, name='new_game'),
    # Page for adding a new review
    path('new_review/<int:game_id>/', views.new_review, name='new_review'),
    # Page for editing an review.
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
]
