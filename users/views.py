from rest_framework.views import APIView, Response, Request, status
from users.models import User
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
