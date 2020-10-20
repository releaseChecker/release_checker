import pytest
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse

from tests.base_classes import DeleteTest
from user.models import Tag


def test_create_tag(authenticated_client, live_server, new_library):
    data = {
        "library": new_library.id
    }
    response = authenticated_client.post(live_server.url + reverse("tag-list"), data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Tag.objects.get(
        user=get_user_model().objects.get(username="test"),
        library=new_library.id
    )


class TestDeleteTag(DeleteTest):
    model = Tag

    @pytest.fixture
    def obj(self, new_tag):
        return new_tag


def test_list_tag(authenticated_client, live_server, libraries, tags):
    response = authenticated_client.get(live_server.url + reverse("tag-list"))
    assert response.status_code == status.HTTP_200_OK

    response_libs = [resp["library"] for resp in response.json()]
    for i, response_lib in enumerate(response_libs):
        library = libraries[i]
        for key, value in response_lib.items():
            assert value == getattr(library, key)

    for tag in tags:
        assert tag.user.username == "test"
