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
    rating =  models.CharField(max_length=20, choices=AgeRestriction.choices, default=AgeRestriction.G)
    synopsis = models.TextField(default=None, null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movies")
    order = models.ManyToManyField("users.User", through="movies.MovieOrder")

class MovieOrder(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="buys")
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="movie_sold")
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

 
