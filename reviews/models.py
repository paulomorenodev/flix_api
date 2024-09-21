from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, '0 estrelas é o mínimo'),
            MaxValueValidator(5, '5 estrelas é o máximo')
        ]
    )
    comment = models.TextField(null=True, blank=True)   

    def __str__(self):
        return f'{self.movie} ({self.stars})'
    