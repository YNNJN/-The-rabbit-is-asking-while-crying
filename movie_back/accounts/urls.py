from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<str:username>/follow/', views.follow, name="follow"),
]