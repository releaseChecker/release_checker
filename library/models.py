from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=50, unique=True)
    version = models.CharField(max_length=20, blank=True, default="0.0.0")
    url = models.CharField(max_length=200)
    belong_to = models.CharField(max_length=20)

    def get_name(self):
        return self.name

    def get_version(self):
        return self.version

    def get_url(self):
        return self.url

    def get_id(self):
        return self.id

    def set_version(self, version):
        self.version = version

    def get_belong_to(self):
        return self.belong_to
