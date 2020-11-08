from django.contrib.auth.models import AbstractUser
from django.db import models

from library.models import History, Library


class User(AbstractUser):
    pass


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="tags")
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="tags")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "library"], name="unique_tagging"),
        ]


class Comment(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="comments")
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
