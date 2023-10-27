from django.urls import path
from booksApp import views

urlpatterns = [
    path('audiobook/', views.audiobooksApi),
    path('audiobook/<str:id>/', views.audiobooksApi),
]