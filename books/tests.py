from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_date="2023-01-01",
            isbn="1234567890123"
        )
        self.book_url = reverse('book_detail', kwargs={'pk': self.book.id})

    def test_create_book(self):
        url = reverse('book_list_create')
        data = {"title": "New Book", "author": "New Author", "publication_date": "2023-02-01", "isbn": "9876543210987"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_books(self):
        url = reverse('book_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        data = {"title": "Updated Book", "author": "Updated Author", "publication_date": "2023-03-01",
                "isbn": "1234567890123"}
        response = self.client.put(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
