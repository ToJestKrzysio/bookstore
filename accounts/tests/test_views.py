import pytest
from django.urls import reverse
from django.test import Client

from accounts.forms import CustomUserCreationForm


@pytest.mark.parametrize("url", [
    "/accounts/signup/",
    reverse("accounts:signup"),
])
def test_signup_status_code(client, url):
    response = client.get(url)
    assert response.status_code == 200


def test_signup_template(get_signup_response):
    assert ("registration/signup.html" in
            [template.name for template in get_signup_response.templates])
    assert ("Create New Account" in
            get_signup_response.content.decode("UTF-8"))


# def test_signup_form():
#     # client = Client(enforce_csrf_checks=True)
#     # response = client.get(reverse("accounts:signup"))
#     form = response.context.get("form")
#     assert isinstance(form, CustomUserCreationForm)
#     assert "csrfmiddlewaretoken" in response

