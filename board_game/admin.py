from django.contrib import admin

# Registering a topic with admin site
from .models import BoardGame
admin.site.register(BoardGame)
