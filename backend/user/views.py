from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from library.models import History
from library.serializers import HistorySerializer
from user.models import Tag, User
from user.serializers import ListTagSerializer, CreateTagSerializer, DeleteTagSerializer, UserSerializer


class TagViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return self.request.user.tags.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateTagSerializer
        elif self.action == 'list':
            return ListTagSerializer
        elif self.action == 'histories':
            return HistorySerializer
        return DeleteTagSerializer

    def perform_create(self, serializer):
        if not Tag.objects.filter(
                user=self.request.user,
                library=self.request.data["library"]
        ).exists():
            serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def histories(self, request):
        tags = request.user.tags.all().values("library")
        histories_in_tags = History.objects.filter(library__in=tags)
        serializer = self.get_serializer(histories_in_tags, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
