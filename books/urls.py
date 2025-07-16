from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books),
    path('order/', views.place_order),
]
