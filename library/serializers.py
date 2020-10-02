from rest_framework import serializers

from .models import Library


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = [
            "id",
            "name",
            "version",
            "url",
            "belong_to",
            ]
