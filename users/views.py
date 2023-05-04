from rest_framework.views import APIView, Response, Request, status
from users.models import User
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
