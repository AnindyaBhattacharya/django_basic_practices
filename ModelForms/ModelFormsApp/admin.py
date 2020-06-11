from django.contrib import admin
from . import models

# Register your models here.
class MovieDB_View(admin.ModelAdmin):
    list_display=["movie","release","hero","herione","type","points"]

admin.site.register(models.MovieDB,MovieDB_View)
