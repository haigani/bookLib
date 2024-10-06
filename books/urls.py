from django.urls import path
from .views import BookDetailView, BookListCreateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name="book_list_create"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="book_detail"),
]
