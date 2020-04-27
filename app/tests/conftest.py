import pytest


@pytest.fixture(scope="function")
def get_user(django_user_model):
    def _add_user():
        try:
            user = django_user_model.objects.get(
                email="example@example.com"
            )
        except django_user_model.DoesNotExist:
            user = django_user_model.objects.create_user(
                email="example@example.com",
                password="foo",
            )

        return user

    return _add_user


@pytest.fixture(scope="function")
def add_user(django_user_model):
    def _add_user(email, password):
        user = django_user_model.objects.create_user(
            email=email,
            password=password,
        )

        return user

    return _add_user


@pytest.fixture(scope="function")
def add_superuser(django_user_model):
    def _add_superuser(email, password):
        user = django_user_model.objects.create_user(
            email=email,
            password=password,
            is_superuser=True
        )

        return user

    return _add_superuser
