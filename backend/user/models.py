from django.contrib.auth.models import AbstractUser
from django.db import models

from library.models import Library


class User(AbstractUser):
    pass


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="tags")
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="tags")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "library"], name="unique_tagging"),
        ]
