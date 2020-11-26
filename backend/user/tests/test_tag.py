import pytest
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse

from library.tests.test_history import TestListHistory
from tests.base_classes import DeleteTest, ListTest, PathFinder
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


class TestListTag(ListTest):
    model = Tag
    fields = ["id", "library"]

    @pytest.fixture
    def objs(self, tags):
        return tags

    def _check_response_values(self, tags):
        response_libs = [resp["library"] for resp in self.response.json()]
        for i, response_lib in enumerate(response_libs):
            library = tags[i].library
            for key, value in response_lib.items():
                assert value == getattr(library, key)

    def _check_additionally(self, objs):
        self._check_owner_of_tags()

    def _check_owner_of_tags(self):
        response_tag_ids = [resp["id"] for resp in self.response.json()]
        for tag_id in response_tag_ids:
            assert Tag.objects.get(id=tag_id).user.username == "test"


@pytest.fixture
def tagged_histories(new_user, histories):
    library = histories[0].library
    Tag.objects.create(user=new_user, library=library)
    return histories


# need sorted test_case
@pytest.mark.a
class TestListTagHistory(TestListHistory):
    model = Tag
    path_finder = PathFinder("histories")

    @pytest.fixture
    def objs(self, tagged_histories):
        return tagged_histories

    def _check_additionally(self, objs):
        self._check_histories_belong_to_correct_tag(objs)

    def _check_histories_belong_to_correct_tag(self, objs):
        raise NotImplementedError



