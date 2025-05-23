from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('add/', views.add_book, name='add-book'),
    path('edit/<int:pk>/', views.edit_book, name='edit-book'),
    path('delete/<int:pk>/', views.delete_book, name='delete-book'),
]