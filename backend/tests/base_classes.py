import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class DeleteTest:
    model = None

    # should implement obj fixture in TestClass

    def test_delete_basic(self, authenticated_client, live_server, obj):
        response = authenticated_client.delete(
            live_server.url + PathFinder.get_request_path(obj, self.model))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not self.model.objects.filter(id=obj.id)


class UpdateTest:
    model = None

    # should implement obj fixture in TestClass
    # should implement update_data fixture in TestClass

    def test_update_basic(self, authenticated_client, live_server, obj, update_data):
        response = authenticated_client.patch(
            live_server.url + PathFinder.get_request_path(obj, self.model),
            data=update_data,
        )
        assert response.status_code == status.HTTP_200_OK

        updated_library = self.model.objects.get(id=obj.id)
        for key, value in update_data.items():
            assert value == getattr(updated_library, key)


class PathFinder:

    @staticmethod
    def get_request_path(obj, model):
        return reverse(
            f"{model.__name__.lower()}-detail", kwargs={"pk": obj.id})
