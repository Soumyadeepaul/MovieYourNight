from django.db import models

# Create your models here.
class details(models.Model):
    imdb_link=models.TextField(null=True)
    image_link = models.TextField(null=True)
    rating = models.FloatField(null=True)
    metascore = models.FloatField(null=True)
    description = models.TextField(null=True)
    votes = models.FloatField(null=True)
    movie_name = models.TextField(null=True)
    start_year = models.IntegerField(null=True)
    end_year = models.IntegerField(null=True)
    gross = models.FloatField(null=True)
    certificate=models.TextField(null=True)
    time=models.IntegerField(null=True)
    genre=models.TextField(null=True)
    director = models.TextField(null=True)
    stars = models.TextField(null=True)
    status = models.TextField(null=True)
    certificate_meaning=models.TextField(null=True)
    comedy=models.IntegerField(null=True)
    sci_fi= models.IntegerField(null=True)
    horror= models.IntegerField(null=True)
    romance= models.IntegerField(null=True)
    action=models.IntegerField(null=True)
    thriller=models.IntegerField(null=True)
    drama= models.IntegerField(null=True)
    mystery=models.IntegerField(null=True)
    crime=models.IntegerField(null=True)
    animation=models.IntegerField(null=True)
    adventure=models.IntegerField(null=True)
    fantasy= models.IntegerField(null=True)
    family= models.IntegerField(null=True)
    biography=models.IntegerField(null=True)
    docum=models.IntegerField(null=True)
    film_noir= models.IntegerField(null=True)
    history=models.IntegerField(null=True)
    music =models.IntegerField(null=True)
    musical= models.IntegerField(null=True)
    short= models.IntegerField(null=True)
    sport=models.IntegerField(null=True)
    superhero=models.IntegerField(null=True)
    war= models.IntegerField(null=True)
    western=models.IntegerField(null=True)
    tag=models.TextField(null=True)



    def __str__(self):
        return f"{self.movie_name}"



class form(models.Model):
    age=models.IntegerField(null=True)
    year=models.IntegerField(null=True)
    genre=models.TextField(null=True)
    movie=models.TextField(null=True)