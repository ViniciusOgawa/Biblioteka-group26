from rest_framework import serializers
from .models import Copy


class CopySerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField(read_only=True, source="book.id")

    class Meta:
        model = Copy
        fields = ["id", "name", "author", "book_id"]

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)
