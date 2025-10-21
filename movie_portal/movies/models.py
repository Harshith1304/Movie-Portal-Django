from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    poster_image = models.ImageField(upload_to='posters/', blank=True, null=True)
    def __str__(self):
        return self.title

    def get_poster(self):
        """Return uploaded poster, else URL, else default."""
        if self.poster_image:
            return self.poster_image.url
        if self.poster_url:
            return self.poster_url
        return static('movies/default_poster.jpg')

    get_poster = property(get_poster)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} ({self.rating}/5)"
