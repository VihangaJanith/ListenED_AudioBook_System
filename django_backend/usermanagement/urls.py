from django.urls import path
from usermanagement import views

urlpatterns = [
    path('usermanagement/', views.usermanagementApi),
    path('usermanagement/<str:id>/', views.usermanagementApi),
]