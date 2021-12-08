from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from functools import reduce
from django.contrib.auth.models import User

class BoardGame(models.Model):
    """A game user can borrow."""
    name = models.CharField(max_length=200)
    information = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modifier = models.DateTimeField(auto_now=True)
    owner= models.ForeignKey(User, on_delete = models.CASCADE,)
    borrower = models.ForeignKey(User, on_delete = models.SET_NULL, null=True,  blank=True, related_name = "borrower")


    LOAN_STATUS = (
            ('m', 'Maintenance'),
            ('o', 'On loan'),
            ('a', 'Available'),
        )

    status = models.CharField(
            max_length=1,
            choices=LOAN_STATUS,
            blank=True,
            default='m',
            help_text='Book availability',
        )

    def __str__(self):
        """Return a string representation of the models."""
        return self.name

    @property
    def average_score(self):
       """
       Calculates average review score via reduce function
       Function reduces values from a list one by one, adding them to a variable
       Takes 3 parameters: function used to accumulate sum variable, list of values and starting value
       """
       return reduce(lambda sum, item: sum + item.score, self.review_set.all(), 0) / len(self.review_set.all())


class Review(models.Model):
    """A review a user can write for a boardgame."""
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    text = models.TextField()
    score = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_modifier = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
