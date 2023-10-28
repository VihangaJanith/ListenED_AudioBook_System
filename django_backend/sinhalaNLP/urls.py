from django.urls import path
from sinhalaNLP import views

urlpatterns = [
    path('students/', views.sinhalaAudioApi),
    path('students/<str:id>/', views.sinhalaAudioApi),
    path('gettext/', views.textGetbyPost),
    path('predict/', views.predictword),
    path('svc/', views.svct),
    path('audiobooks/', views.audioBook)
]
