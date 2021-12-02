from django.contrib import admin

# Registering a topic with admin site
from .models import BoardGame, Review
admin.site.register(BoardGame)
admin.site.register(Review)
