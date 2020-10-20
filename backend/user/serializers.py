from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from library.serializers import LibrarySerializer
from user.models import Tag, User


class ListTagSerializer(serializers.ModelSerializer):
    library = LibrarySerializer(read_only=True)

    class Meta:
        model = Tag
        fields = [
            "id",
            "library",
        ]


class CreateTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = [
            "library",
        ]


class DeleteTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = [
            "id",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password"
        ]

    def validate_password(self, value):
        return make_password(value)
