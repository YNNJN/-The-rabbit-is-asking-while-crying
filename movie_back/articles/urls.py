from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('hits/<int:article_pk>/', views.hits, name='hits'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comment_create/', views.comment_create, name="comment_create"),
]
