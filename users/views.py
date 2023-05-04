from rest_framework.views import APIView, Request, Response, status

from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsUserColaboratorOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from books.models import Book
from django.shortcuts import get_object_or_404


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserColaboratorOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    url_params_name = "pk"


class UserFollowView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        book_obj = get_object_or_404(Book, id=pk)

        if request.user.books_following.filter(id=pk).exists():
            return Response(
                {"mensagem": f"You are already following the book {book_obj.name}."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        request.user.books_following.add(book_obj)
        book_obj.followers.add(request.user)

        return Response(
            {"mensagem": f"You are following the book {book_obj.name}."},
            status=status.HTTP_200_OK,
        )
