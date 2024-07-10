from django.urls import path
from .views import book_cylinder
from . import views

urlpatterns = [
    path('api/book-cylinder', book_cylinder, name='book-cylinder'),

    path('', views.index, name='index'),
    
]

