from rest_framework import viewsets
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
        return DeleteTagSerializer

    def perform_create(self, serializer):
        if not Tag.objects.filter(
                user=self.request.user,
                library=self.request.data["library"]
        ).exists():
            serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
