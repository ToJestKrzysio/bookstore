import pytest
from django.urls import reverse


# def test_homepage_status_code(client):
#     response = client.get("/")
#     assert response.status_code == 200


@pytest.mark.parametrize("url", [
    "/",
    reverse('home:home')
])
def test_homepage_status_code_by_reverse(client, url):
    # url = reverse('home:home')
    response = client.get(url)
    assert response.status_code == 200
