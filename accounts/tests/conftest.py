from django.urls import reverse
from pytest import fixture


@fixture()
def get_signup_response(client, db):
    url = reverse("account_signup")
    return client.get(url)
