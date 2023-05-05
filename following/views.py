from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404
from following.models import Follow
from following.serializers import FollowSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class FollowView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, book_id: int) -> Response:
        book_obj = get_object_or_404(Follow, id=book_id)
        serializer = FollowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(book=book_obj, user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
