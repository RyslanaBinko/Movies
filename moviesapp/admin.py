from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html

from .models import Movie, Genre, Status


class MovieAdmin(ModelAdmin):

    list_display = ("title", "genres", "movies_picture", "status1")

    def movies_picture(self, object):  # noqa
        picture = ""
        if object.picture:
            picture = format_html("<img src ='{url}' alt= '{{ title }}' width=100>",
                                  url=object.picture, title=object.title)
        return picture

    def genres(self, object):  # noqa
        if object.genre.all():
            return ", ".join([genre.title for genre in object.genre.all()])

    def status1(self, object):  # noqa
        if object.status.all():
            return ", ".join([status.title for status in object.status.all()])


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Status)
