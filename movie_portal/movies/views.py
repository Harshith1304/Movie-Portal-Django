from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from datetime import datetime
from .models import Movie

# 🎬 Home Page – search + filter
def home(request):
    query = request.GET.get('q', '')
    genre_filter = request.GET.get('genre', '')
    year_filter = request.GET.get('year', '')
    rating_filter = request.GET.get('rating', '')

    # Fetch all movies, latest first
    movies = Movie.objects.all().order_by('-id')

    # Filter lists for dropdowns
    genres = Movie.objects.values_list('genre', flat=True).distinct()
    
    # Generate years from current year down to 1950
    current_year = datetime.now().year
    years = list(range(current_year, 1949, -1))
    
    ratings = [str(i) for i in range(10, 0, -1)]  # For rating filter dropdown

    # Apply filters
    if query:
        movies = movies.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if genre_filter:
        movies = movies.filter(genre=genre_filter)
    if year_filter:
        movies = movies.filter(release_year=year_filter)
    if rating_filter:
        movies = movies.filter(rating__gte=rating_filter)

    return render(request, 'movies/home.html', {
        'movies': movies,
        'genres': genres,
        'years': years,
        'ratings': ratings,
        'query': query,
        'genre_filter': genre_filter,
        'year_filter': year_filter,
        'rating_filter': rating_filter,
    })

# 🎥 Movie Detail Page
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    recommendations = Movie.objects.filter(genre=movie.genre).exclude(id=movie.id)[:5]

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'recommendations': recommendations
    })
