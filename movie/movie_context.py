from .models import Movie

def slider_movies(request):
    movies = Movie.objects.all().order_by('title')[0:4]
    #movies = Movie.objects.last()
    return {'slider_movie': movies}