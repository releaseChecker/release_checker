from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .crawler import LibraryCrawlerFactory
from .models import Library
from .serializers import LibrarySerializer, CreateLibrarySerializer, DeleteLibrarySerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return LibrarySerializer
        if self.action == "delete":
            return DeleteLibrarySerializer
        return CreateLibrarySerializer


class CrawlingAPIView(APIView):

    def get(self, request):
        libraries = Library.objects.all()
        for library in libraries:
            LibraryCrawlerFactory.get_crawler(library).crawl()
        return Response()
