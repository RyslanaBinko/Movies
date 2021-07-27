from django.views.generic import ListView

from moviesapp.models import Movie


class MovieView(ListView):

    context_object_name = 'object_list'
    queryset = Movie.objects.filter(status__title__in=('Не просмотрено',)).order_by('?')[:1]
    template_name = 'index.html'


class TestView(ListView):

    context_object_name = 'object_list'
    queryset = Movie.objects.filter(status__title__in=('Не просмотрено',)).order_by('?')[:1]
    template_name = 'test.html'
