from rest_framework.views import APIView, Request, Response, status

from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsUserColaboratorOrReadOnly
from rest_framework import generics


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserColaboratorOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    url_params_name = "pk"




