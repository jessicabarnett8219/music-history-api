from django.db import models

class Artist(models.Model):
  name = models.CharField(default="", max_length=100)
  birth_date = models.CharField(default="", max_length=100)
  biggest_hit = models.CharField(default="", max_length=100)

  def __str__(self):
    return self.name

class Album(models.Model):
  title = models.CharField(max_length=100)
  year_released = models.CharField(max_length=4)

  def __str__(self):
    return self.title

class Song(models.Model):
  title = models.CharField(default="", max_length=100)
  albums = models.ForeignKey(Album, on_delete=models.CASCADE)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.__dict__)


