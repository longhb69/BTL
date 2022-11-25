from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie

# Create your views here.


class HomeView(ListView):
    model = Movie
    template_name = 'movie/home.html'
    paginate_by = 1 
    
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status='MW')
        context['recently_added'] = Movie.objects.filter(status='RA')
        return context


class MovieList(ListView):
    model = Movie
    paginate_by = 1 

class MovieDetail(DetailView):
    model = Movie
    
    def render_to_response(self, *args, **kwargs):
        self.object.views_count += 1
        self.object.save()
        return super().render_to_response(*args, **kwargs)
    
    def get_context_data(self , **kwargs):
        context = super(MovieDetail , self).get_context_data(**kwargs)
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category)
        return context
    
class MovieCategory(ListView):
    model = Movie
    
    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)
    
    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context
    
class MovieSearch(ListView):
    model = Movie
    paginate_by = 1

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        
        else:
            object_list = self.model.objects.none()

        return object_list
            
class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True
   

    
   
    
    
    
       