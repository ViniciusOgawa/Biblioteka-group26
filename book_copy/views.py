from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsUserColaboratorOrReadOnly
from .serializers import CopySerializer
from .models import Copy
from books.models import Book
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class CopyView(ListCreateAPIView):
    serializer_class = CopySerializer
    pagination_class = PageNumberPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserColaboratorOrReadOnly]

    def get_queryset(self):
        book_id = self.kwargs.get("pk")
        return Copy.objects.filter(book_id=book_id)
    
    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        copies = request.data.get('copies')
        if copies is None:
            return Response({"error": "Número de cópias não fornecido."}, status=400)
        for _ in range(copies):
            book_copy = Copy(book=book)
            book_copy.save()
        return Response({"success": f"{copies} cópias do livro {pk} cadastradas com sucesso."}, status=200)
