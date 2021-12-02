from django.db import models

class BoardGame(models.Model):
    #A game user can borrow
    name = models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_now_add=True)

    date_modifier = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return a string representation of the models
        return self.name

class Review(models.Model):
    boardgame = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_Add=True)

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        # Return a string representation of the model
        return f'{self.text[:50]}...'
