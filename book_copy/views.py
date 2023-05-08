from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CopySerializer
from .models import Copy


class CopyView(ListAPIView):
    serializer_class = CopySerializer
    pagination_class = PageNumberPagination
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        book_id = self.kwargs.get("pk")
        return Copy.objects.filter(book_id=book_id)
