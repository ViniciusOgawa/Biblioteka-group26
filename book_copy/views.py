from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from .serializers import CopySerializer
from .models import Copy
from books.models import Book
from django.shortcuts import get_object_or_404
from books.permissions import IsLybrarian


class CopyView(ListCreateAPIView):
    serializer_class = CopySerializer
    pagination_class = PageNumberPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get_queryset(self):
        book_id = self.kwargs.get("pk")
        return Copy.objects.filter(book_id=book_id)
    
    def perform_create(self, serializer: Copy):
        book_id = self.kwargs.get("pk")
        get_object_or_404(Book, id=book_id)
        return serializer.save(book_id=book_id)
