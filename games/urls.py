from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('<int:id>/', views.game_detail, name='game_detail'),
    path('create/', views.game_create, name='game_create'),
    path('<int:id>/edit/', views.game_update, name='game_update'),
    path('<int:id>/delete/', views.game_delete, name='game_delete'),
]