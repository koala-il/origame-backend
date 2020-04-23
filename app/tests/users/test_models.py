import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(email="normal@user.com", password="foo")

    assert user.email == "normal@user.com"
    assert str(user) == "normal@user.com"
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False


@pytest.mark.django_db
def test_create_superuser():
    User = get_user_model()
    admin_user = User.objects.create_superuser("super@user.com", "foo")

    assert admin_user.email == "super@user.com"
    assert admin_user.is_active is True
    assert admin_user.is_staff is True
    assert admin_user.is_superuser is True


@pytest.mark.django_db
def test_create_superuser_not_staff():
    User = get_user_model()
    admin_user = None
    try:
        admin_user = User.objects.create_superuser(
            "super@user.com",
            "foo",
            is_staff=False
        )
    except ValueError as e:
        assert isinstance(e, ValueError)
        assert admin_user is None

    assert User.objects.all().count() == 0


@pytest.mark.django_db
def test_create_superuser_not_superuser():
    User = get_user_model()
    admin_user = None
    try:
        admin_user = User.objects.create_superuser(
            "super@user.com",
            "foo",
            is_superuser=False
        )
    except ValueError as e:
        assert isinstance(e, ValueError)
        assert admin_user is None

    assert User.objects.all().count() == 0


@pytest.mark.django_db
def test_create_user_no_email():
    User = get_user_model()
    admin_user = None
    try:
        admin_user = User.objects.create_user(
            None,
            "foo"
        )
    except ValueError as e:
        assert isinstance(e, ValueError)
        assert admin_user is None

    assert User.objects.all().count() == 0
