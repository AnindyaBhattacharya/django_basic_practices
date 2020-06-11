from django.db import models

# Create your models here.
class MovieDB(models.Model):
    type = [("movie","movie"),("flix","netflix"),("prime","amazon prime"),("hotstar","hotstar")]
    movie = models.CharField(max_length=30)
    release = models.DateField()
    hero = models.CharField(max_length=30)
    herione = models.CharField(max_length=30)
    type = models.CharField(max_length=30,db_column="Show_Type",choices=type)
    points = models.IntegerField(db_column="Rating",default=0)
