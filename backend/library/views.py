from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .crawler import LibraryCrawlerFactory
from .models import Library, History
from .serializers import LibrarySerializer, CreateLibrarySerializer, DeleteLibrarySerializer, HistorySerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return LibrarySerializer
        elif self.action == "delete":
            return DeleteLibrarySerializer
        elif self.action == "histories":
            return HistorySerializer
        return CreateLibrarySerializer

    @action(detail=True, methods=['get'])
    def histories(self, request, pk):
        queryset = History.objects.filter(library=pk).order_by('-version')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CrawlingAPIView(APIView):

    def get(self, request):
        libraries = Library.objects.all()
        for library in libraries:
            LibraryCrawlerFactory.get_crawler(library).crawl()
        return Response()


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
