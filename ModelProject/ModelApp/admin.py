from django.contrib import admin
from ModelApp.models import Job,Book,Student
# Register your models here.

class JobView(admin.ModelAdmin):
    list_display = ['PostingDate','Location','Salary','Qualification']
class BookView(admin.ModelAdmin):
    list_display = ['Number','Title','Author','PublishedDate']
class StudentView(admin.ModelAdmin):
    list_display = ['name',"dept","roll"]

admin.site.register(Job,JobView)
admin.site.register(Book,BookView)
admin.site.register(Student,StudentView)
