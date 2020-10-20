import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from library.models import Library
from tests.base_classes import DeleteTest, UpdateTest


def test_create_library(authenticated_client, live_server):
    data = {
        "name": "test",
        "version": "1.0.0",
        "url": "test.com",
        "group": "test_group"
    }

    response = authenticated_client.post(
        live_server.url + reverse("library-list"), data, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    assert Library.objects.get(name=data["name"])


class TestUpdateLibrary(UpdateTest):
    model = Library

    @pytest.fixture
    def update_data(self):
        return {
            "version": "2.0.0",
            "url": "test1.com",
            "group": "python",
        }

    @pytest.fixture
    def obj(self, new_library):
        return new_library


def test_detail_library(authenticated_client, live_server, new_library):
    response = authenticated_client.get(
        live_server.url + reverse("library-detail", kwargs={"pk": new_library.id}))
    assert response.status_code == status.HTTP_200_OK

    fields = list(response.json().keys())
    assert ["id", "name", "url"] == fields

    for key, value in response.json().items():
        assert value == getattr(new_library, key)


class TestDeleteLibrary(DeleteTest):
    model = Library

    @pytest.fixture
    def obj(self, new_library):
        return new_library


def test_list_library(authenticated_client, live_server, libraries):
    response = authenticated_client.get(live_server.url + reverse("library-list"))
    assert response.status_code == status.HTTP_200_OK

    # check returned fields
    fields = list(response.json()[0].keys())
    assert ["id", "name", "url"] == fields

    # check response values
    for i, response_lib in enumerate(response.json()):
        library = libraries[i]
        for key, value in response_lib.items():
            assert value == getattr(library, key)
