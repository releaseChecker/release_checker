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
        if items["latest_version"] != self.library.get_version():
            self.library.version = items["latest_version"]
            self._update_version()

    def _update_version(self):
        url = f"http://localhost:8000/libraries/{self.library.get_id()}/"
        serialized_library = LibrarySerializer().to_representation(self.library)
        requests.put(
            url=url,
            data=serialized_library
        )


class MavenLibraryCrawler(LibraryCrawler):

    def _parse(self, response):
        items = {}
        page = BeautifulSoup(response, features="lxml")
        items["latest_version"] = page.find("a", class_="vbtn release").string
        return items


class LibraryCrawlerFactory:

    @staticmethod
    def get_crawler(library):
        if library.get_belong_to() == "maven":
            return MavenLibraryCrawler(library)
