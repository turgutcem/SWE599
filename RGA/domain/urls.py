from django.urls import path
from . import views

app_name = 'domain'

urlpatterns = [
    path('play/', views.play_view, name='play'),
    path('create/', views.create_view, name='create'),
]
