from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True, source="user.id")
    copy_id = serializers.IntegerField(read_only=True, source="copy.id")

    class Meta:
        model = Loan
        fields = ["id", "return_date", "user_id", "copy_id", "returned", "loan_date"]

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)
