from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Library, History
from .library_version import LibraryVersion


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = [
            "id",
            "name",
            "url",
            ]


class CreateLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = [
            "name",
            "version",
            "url",
            "group",
        ]

    def validate_version(self, version):
        for i, c in enumerate(version):
            if c.isdigit():
                version = version[i:]
                break
        if not LibraryVersion(version).is_valid():
            raise ValidationError("version data should be '0.0.0' pattern")
        return version


class DeleteLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = [
            "id",
        ]


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = [
            "id",
            "library",
            "version",
            "url",
        ]