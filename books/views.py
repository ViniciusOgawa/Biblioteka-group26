from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsUserColaboratorOrReadOnly
from .permissions import IsLybrarian
from .models import Book
from book_copy.models import Copy
from .serializers import BookSerializer


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserColaboratorOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer: Book):
        return serializer.save()


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    lookup_url_kwarg = "book_id"