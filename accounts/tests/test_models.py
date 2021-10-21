import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user():
    user_model = get_user_model()
    user = user_model.objects.create_user(
        username="test_dupa",
        email="testdupa@gmail.com",
        password="dupapass123",
    )
    assert user_model.objects.count() == 1
    assert user.username == "test_dupa"
    assert user.email == "testdupa@gmail.com"
    assert not user.is_superuser
    assert not user.is_staff
    assert user.is_active


@pytest.mark.django_db
def test_create_superuser():
    user_model = get_user_model()
    user = user_model.objects.create_superuser(
        username="test_dupa",
        email="testdupa@gmail.com",
        password="dupapass123",
    )
    assert user_model.objects.filter(is_superuser=True).count() == 1
    assert user.username == "test_dupa"
    assert user.email == "testdupa@gmail.com"
    assert user.is_superuser
    assert user.is_staff
    assert user.is_active
