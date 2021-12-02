# Define URL pattern for board_game

from django.urls import path

from . import views

app_name = 'board_game'

urlpatterns =[
    # Home page
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
]
