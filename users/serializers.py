from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_superuser", "is_librarian"]
        extra_kwargs = {
            "is_superuser": {"read_only": True},
            "password": {"write_only": True},
            "email": {"validators": [UniqueValidator(queryset=User.objects.all())]},
        }

    def create(self, validated_data: dict) -> User:
        if validated_data["is_librarian"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(validated_data["password"])
                instance.save(update_fields=["password"])
            else:
                setattr(instance, key, value)
        instance.save()
        return instance
