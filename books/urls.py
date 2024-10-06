from django.urls import path
from .views import BookDetailView, BookListCreateView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name="book_list_create"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='register')
]
