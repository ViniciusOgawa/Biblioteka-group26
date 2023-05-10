from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from loans.models import Loan
from book_copy.models import Copy
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from loans.serializers import LoanSerializer
from users.models import User
from loans.permissions import IsUserColaboratorOrReadOnly


class LoanView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserColaboratorOrReadOnly]
    serializer_class = None

    def post(self, request, user_id, book_id):
        user_obj = get_object_or_404(User, id=user_id)
        book_copy_obj = get_object_or_404(Copy, id=book_id)

        if book_copy_obj.is_rented:
            return Response(
                {"message": "A cópia do livro já está alugada."}, status=400
            )

        book_copy_obj.is_rented = True
        book_copy_obj.save()

        return_date = datetime.now().date() + timedelta(days=3)

        loan = Loan.objects.create(
            user=user_obj, copy=book_copy_obj, return_date=return_date
        )

        serializer = LoanSerializer(loan)
        return Response(serializer.data, status=201)


class LoanHistoryView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserColaboratorOrReadOnly]
    serializer_class = None

    def get(self, request):
        loans = Loan.objects.filter(user=request.user.id)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)


class LoanDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserColaboratorOrReadOnly]
    serializer_class = None

    def put(self, request, loan_id):
        loan = get_object_or_404(Loan, id=loan_id)

        if loan.returned:
            return Response(
                {"error": "O livro já foi entregue anteriormente."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        loan.returned = True
        loan.save()

        return Response({"success": "Livro recebido com sucesso."})
