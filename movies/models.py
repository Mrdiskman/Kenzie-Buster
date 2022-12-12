from django.db import models

class AgeRestriction(models.TextChoices):
    G = "G"
    PG = "PG"
    PGTHIRTEEN= "PG-13"
    R = "R"
    NC = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating =  models.CharField(max_length=20, null=True, choices=AgeRestriction.choices, default=AgeRestriction.G)
    synopsis = models.TextField(default=None, null=True)
