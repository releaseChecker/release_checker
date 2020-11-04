import pytest
from django.urls import reverse
from rest_framework import status

from library.models import History
from tests.base_classes import DeleteTest, PathFinder, ListTest


# def test_create_history(authenticated_client, live_server, new_library):
#     data = {
#         "library": new_library.id,
#         "version": "1.0.0",
#         "url": "history.com",
#     }
#
#     response = authenticated_client.post(
#         live_server.url +
#         reverse("history-list", kwargs={"library_id": new_library.id}),
#         data, format="json")
#     assert response.status_code == status.HTTP_201_CREATED
#
#     assert History.objects.get(library=data["library"],
#                                version=data["version"],
#                                url=data["url"])


# class TestDeleteHistory(DeleteTest):
#     model = History
#     path_finder = PathFinder("detail", related="library")
#
#     @pytest.fixture
#     def obj(self, new_history):
#         return new_history


# 해당 라이브러리에 대한 history의 버전이 유니크해야 함
# 정렬 검사가 필요

class TestListHistory(ListTest):
    model = History
    fields = ["id", "library", "version", "url"]

    @pytest.fixture
    def objs(self, histories):
        return histories

    def _check_response_values(self, histories):
        for i, response_history in enumerate(self.response.json()):
            history = histories[i]
            for key, value in response_history.items():
                if key == "library":
                    assert value == getattr(history, key).id
                else:
                    assert value == getattr(history, key)
