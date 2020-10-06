from django.db import models

from library.library_version import LibraryVersion


class Library(models.Model):
    name = models.CharField(max_length=50, unique=True)
    version = models.CharField(max_length=20)
    url = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=20)

    def get_url(self):
        return self.url

    def is_up_to_date(self, latest_version):
        current = LibraryVersion(self.version)
        latest = LibraryVersion(latest_version)
        return not current.is_older_than(latest)

    def is_member_of(self, affiliation):
        return self.affiliation == affiliation


