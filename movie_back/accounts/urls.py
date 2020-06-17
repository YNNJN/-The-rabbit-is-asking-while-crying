from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/follow/', views.follow, name="follow"),
    path('get/', views.get, name="get")
]