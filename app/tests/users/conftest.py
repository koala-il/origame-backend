import pytest
from django.contrib.auth import get_user_model


@pytest.fixture(scope="function")
def add_user():
    def _add_user():
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")

        return user

    return _add_user
