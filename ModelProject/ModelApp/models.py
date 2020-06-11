from django.db import models

# Create your models here.
class Job(models.Model):
    PostingDate = models.DateField(db_column="Posting Date")
    Location = models.CharField(max_length=30)
    Salary = models.FloatField()
    Qualification = models.CharField(max_length=30)

class Book(models.Model):
    Number = models.IntegerField()
    Title = models.CharField(max_length=30)
    Author = models.CharField(max_length=30)
    PublishedDate = models.DateField()

class Student(models.Model):
    dept_choice = [("ME","Mechanical"),("ECE","Electronics"),("EE","Electrical")]
    name = models.CharField(max_length=30,db_column="Student Name")
    dept = models.CharField(max_length=30,db_column="Department",choices=dept_choice)
    roll = models.IntegerField()
