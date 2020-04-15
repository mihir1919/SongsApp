from django.db import models
from django.urls import reverse

class Album(models.Model):
    artist=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    logo=models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + "->" + self.artist


class Songs(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    sname=models.CharField(max_length=200)
    type=models.CharField(max_length=10)
    isfav=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.sname