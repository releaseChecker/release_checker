from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Library
from .library_version import LibraryVersion


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = [
            "id",
            "name",
            "version",
            "url",
            ]

    def validate_version(self, version):
        for i, c in enumerate(version):
            if c.isdigit():
                version = version[i:]
                break
        if not LibraryVersion(version).is_valid():
            raise ValidationError("version data should be '0.0.0' pattern")
        return version
