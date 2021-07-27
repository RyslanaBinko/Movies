from django.contrib import admin
from django.urls import path

from moviesapp.views import MovieView, TestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie', MovieView.as_view(), name='movie_view'),
    path('test', TestView.as_view(), name='test_view'),
]
