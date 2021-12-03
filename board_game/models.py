from django.db import models

class BoardGame(models.Model):
    """A game user can borrow."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modifier = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the models."""
        return self.name

class Review(models.Model):
    """A review a user can write for a boardgame."""
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modifier = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
