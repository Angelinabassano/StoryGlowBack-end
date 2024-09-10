from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateBook.as_view(), name='create-book'),
    path('list/', views.BookList.as_view(), name='book-list'),
    path('get/<int:pk>/', views.GetBook.as_view(), name='get-book'),
    path('update/<int:pk>/', views.UpdateBook.as_view(), name='update-book'),
    path('delete/<int:pk>/', views.DeleteBook.as_view(), name='delete-book'),
]
