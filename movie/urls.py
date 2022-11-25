from django.urls import path
from django.conf.urls import url
from .views import MovieList,MovieDetail, MovieCategory, MovieSearch, MovieYear
from . import views

app_name = 'movies'

urlpatterns = [
    path('',MovieList.as_view(), name='movie_list'),
    path('category/<str:category>',MovieCategory.as_view(), name='movie_category'),
    path('search/',MovieSearch.as_view(), name='movie_search'),
    path('<slug:slug>',MovieDetail.as_view(), name='movie_detail'),
    path('year/<int:year>',MovieYear.as_view(), name='movie_year'),
    
    

] 
