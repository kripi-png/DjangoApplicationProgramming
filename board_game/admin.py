from django.contrib import admin

# Registering a topic with admin site
from .models import BoardGame
admin.site.register(BoardGame)

class Review(models.Model):
    boardgame = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_Add=True)

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        # Return a string representation of the model
        return f'{self.text[:50]}...'
