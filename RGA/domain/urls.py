from django.urls import path
from . import views

app_name = 'domain'

urlpatterns = [
    path('play/', views.play_view, name='play'),
    path('create/', views.create_view, name='create'),
    path('create_game/', views.create_game, name='create_game'),
    path('play/<int:pk>/', views.play_game_view, name='play_game')
]
