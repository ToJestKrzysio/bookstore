import pytest
from django.urls import reverse


@pytest.mark.parametrize("url", [
    "/accounts/signup/",
    reverse("account_signup"),
])
def test_signup_status_code(client, url, db):
    response = client.get(url)
    assert response.status_code == 200


def test_signup_template(get_signup_response):
    assert ("account/signup.html" in
            [template.name for template in get_signup_response.templates])
    assert ("Create New Account" in
            get_signup_response.content.decode("UTF-8"))
