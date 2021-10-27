import pytest
from django.urls import reverse


@pytest.mark.parametrize("url", [
    "/",
    reverse('home:home')
])
def test_homepage_status_code(client, url):
    response = client.get(url)
    assert response.status_code == 200


def test_homepage_template(get_homepage_response):
    assert ("home/home.html"
            in [template.name for template in get_homepage_response.templates])


def test_homepage_template_correct_html(get_homepage_response):
    assert ("Welcome to the worst bookstore"
            in get_homepage_response.content.decode("UTF-8"))


@pytest.mark.parametrize("url", [
    "/about/",
    reverse('home:about')
])
def test_about_view_status_code(client, url):
    response = client.get(url)
    assert response.status_code == 200


def test_about_view_template(get_about_view_response):
    assert ("home/about.html" in
            [template.name for template in get_about_view_response.templates])
