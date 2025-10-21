# movies/admin.py
from django.contrib import admin
from .models import Movie, Review, Genre
admin.site.register(Review)
admin.site.register(Genre)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year', 'rating')