import pytest
from django.contrib.auth.hashers import make_password
from pytest_django.lazy_django import skip_if_no_django
from rest_framework.reverse import reverse

from library.models import Library
from user.models import Tag


@pytest.fixture
def new_user(django_user_model):
    credential = {
        "username": "test",
        "password": "1234",
    }
    password = make_password(credential["password"])
    user = django_user_model.objects.create(username=credential["username"], password=password)
    return user


@pytest.fixture()
def authenticated_client(token):
    skip_if_no_django()

    from rest_framework.test import APIClient
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
    return client


@pytest.fixture()
def token(django_user_model, client, live_server, new_user):
    data = {
        "username": new_user.username,
        "password": "1234",
    }
    token = client.post(live_server.url + reverse("token_obtain_pair"), data=data).json()["access"]
    return token


@pytest.fixture
def new_library(db):
    return Library.objects.create(
        name="test", version="1.0.0", url="test.com", group="test_group")


@pytest.fixture
def libraries(db):
    count = 3
    libraries = []
    for i in range(count):
        i = str(i)
        library = Library.objects.create(name=i, version=i, url=i, group=i)
        libraries.append(library)
    return libraries


@pytest.fixture
def new_tag(new_user, new_library):
    tag = Tag.objects.create(
        user=new_user,
        library=new_library)
    return tag


@pytest.fixture
def tags(new_user, libraries):
    return [
        Tag.objects.create(user=new_user, library=library)
        for library in libraries
    ]
