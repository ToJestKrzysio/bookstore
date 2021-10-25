from django.urls import reverse
from pytest import fixture


@fixture()
def get_signup_response(client):
    url = reverse("accounts:signup")
    return client.get(url)
