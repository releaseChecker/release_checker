import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class PathFinder:

    def __init__(self, url_suffix, **kwargs):
        self.url_suffix = url_suffix
        self.kwargs = kwargs

    def get_request_path(self, obj, model):
        reverse_kwargs = self._get_reverse_kwargs(obj)
        url_basename = self._get_url_basename(model)
        return reverse(
            f"{url_basename}-{self.url_suffix}",
            kwargs=reverse_kwargs)

    def _get_reverse_kwargs(self, obj):
        reverse_kwargs = {}
        if "related" in self.kwargs:
            reverse_kwargs["pk"] = getattr(obj, self.kwargs["related"]).id
        if self.url_suffix == "detail":
            reverse_kwargs["pk"] = obj.id
        return reverse_kwargs
    
    def _get_url_basename(self, model):
        if "basename" in self.kwargs:
            return self.kwargs["basename"]
        return model.__name__.lower()


class DeleteTest:
    model = None
    path_finder = PathFinder("detail")

    # should implement obj fixture in TestClass
    @pytest.fixture
    def obj(self):
        raise NotImplementedError

    def test_delete_basic(self, authenticated_client, live_server, obj):
        response = authenticated_client.delete(
            live_server.url + self.path_finder.get_request_path(obj, self.model))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not self.model.objects.filter(id=obj.id)


class UpdateTest:
    model = None
    path_finder = PathFinder("detail")

    # should implement obj fixture in TestClass
    @pytest.fixture
    def obj(self):
        raise NotImplementedError

    # should implement update_data fixture in TestClass
    @pytest.fixture
    def update_data(self):
        raise NotImplementedError

    def test_update_basic(self, authenticated_client, live_server, obj, update_data):
        response = authenticated_client.patch(
            live_server.url + self.path_finder.get_request_path(obj, self.model),
            data=update_data,
        )
        assert response.status_code == status.HTTP_200_OK

        updated_library = self.model.objects.get(id=obj.id)
        for key, value in update_data.items():
            assert value == getattr(updated_library, key)


class ListTest:

    model = None
    fields = None
    response = None
    path_finder = PathFinder("list")

    @pytest.fixture
    def objs(self):
        raise NotImplementedError

    def test_list_basic(self, authenticated_client, live_server, objs):
        self.response = self._request(authenticated_client, live_server, objs)
        self._check_status_code()
        self._check_response_fields()
        self._check_response_values(objs)
        self._check_additionally(objs)

    def _request(self, authed_client, live_server, objs):
        return authed_client.get(
            live_server.url +
            self.path_finder.get_request_path(objs[0], self.model)
        )

    def _check_status_code(self):
        assert self.response.status_code == status.HTTP_200_OK

    def _check_response_fields(self):
        response_fields = list(self.response.json()[0].keys())
        assert response_fields == self.fields

    def _check_response_values(self, objs):
        raise NotImplementedError

    def _check_additionally(self, objs):
        pass
