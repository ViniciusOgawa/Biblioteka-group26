from rest_framework import serializers
from following.models import Follow


class FollowSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    book_title = serializers.SerializerMethodField()
    followed_by = serializers.SerializerMethodField()

    def get_book_title(self, obj):
        return obj.book.name

    def get_followed_by(self, obj):
        return obj.user.username

    def create(self, validated_data: dict) -> Follow:
        return Follow.objects.create(**validated_data)
