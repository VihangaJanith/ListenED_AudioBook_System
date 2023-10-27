from django.urls import path
from recommendApp import views

urlpatterns = [
    path('book/', views.bookApi),
    path('book/<str:id>/', views.bookApi),
    path('bookrecommend/', views.bookrecommendApi)
]