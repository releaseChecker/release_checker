import pytest
from rest_framework import status
from rest_framework.reverse import reverse


class TestAuth:

    @pytest.fixture
    def requiring_auth_url(self, live_server):
        return live_server.url + reverse("tag-list")

    def test_no_auth(self, client, requiring_auth_url):
        response = client.get(requiring_auth_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_jwt_auth(self, authenticated_client, requiring_auth_url):
        response = authenticated_client.get(requiring_auth_url)
        assert response.status_code == status.HTTP_200_OK
