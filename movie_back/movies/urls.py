from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<str:movie_id>/', views.detail, name='detail'),
    path('movie/<str:movie_id>/watched/', views.watched, name='watched'),
    path('movie/<str:movie_id>/review_create/', views.review_create, name='review_create'), 
    path('movie/<str:movie_id>/review_delete/', views.review_delete, name='review_delete'),   
]