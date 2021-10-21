import pytest
from django.urls import reverse


@pytest.mark.parametrize("url", [
    "/",
    reverse('home:home')
])
def test_homepage_status_code_by_reverse(client, url):
    response = client.get(url)
    assert response.status_code == 200


def test_homepage_template(get_homepage_response):
    assert "home/home.html" in [template.name for template in get_homepage_response.templates]


def test_homepage_template_correct_html(get_homepage_response):
    assert "Welcome to the worst bookstore ever bitch!" in get_homepage_response.content.decode("UTF-8")

