from abc import ABCMeta, abstractmethod
import requests
from bs4 import BeautifulSoup

from library.serializers import LibrarySerializer


class LibraryCrawler(metaclass=ABCMeta):

    def __init__(self, library):
        self.library = library

    def crawl(self):
        response = requests.get(self.library.get_url()).text
        items = self._parse(response)
        self._process_item(items)
        return items

    @abstractmethod
    def _parse(self, response):
        pass

    def _process_item(self, items):
        if not self.library.is_up_to_date(items["version"]):
            serializer = LibrarySerializer(self.library, data=items, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()


class MavenLibraryCrawler(LibraryCrawler):

    def _parse(self, response):
        items = {}
        page = BeautifulSoup(response, features="lxml")
        items["version"] = page.find("a", class_="vbtn release").string
        return items


class LibraryCrawlerFactory:

    @staticmethod
    def get_crawler(library):
        if library.is_member_of("maven"):
            return MavenLibraryCrawler(library)
