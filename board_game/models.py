from django.db import models

class Boardgame(models.Model):
    #A game user can borrow
    name = models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_now_add=True)

    date_modifier = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return a string representation of the models
        return self.name
