from pytest import fixture
from django.urls import reverse


@fixture
def get_homepage_response(client):
    url = reverse('home:home')
    return client.get(url)


@fixture
def get_about_view_response(client):
    url = reverse('home:about')
    return client.get(url)
