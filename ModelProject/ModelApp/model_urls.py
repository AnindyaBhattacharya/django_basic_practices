from django.contrib import admin
from django.urls import path
from ModelApp import views

urlpatterns = [
    path('job/', views.job),
    path('book/', views.book),
]
