from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ManyToManyField("moviesapp.Genre")
    picture = models.URLField(max_length=500, null=True)
    status = models.ManyToManyField("moviesapp.Status")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
