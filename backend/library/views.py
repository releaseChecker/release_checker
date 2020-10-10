from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .crawler import LibraryCrawlerFactory
from .models import Library
from .serializers import LibrarySerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class CrawlingAPIView(APIView):

    def get(self, request):
        libraries = Library.objects.all()
        for library in libraries:
            LibraryCrawlerFactory.get_crawler(library).crawl()
        return Response()
