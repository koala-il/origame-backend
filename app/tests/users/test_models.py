import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(email='normal@user.com', password='foo')
    assert user.email == 'normal@user.com'
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False
    try:
        # username is None for the AbstractUser option
        # username does not exist for the AbstractBaseUser option
        assert user.username is None
    except AttributeError:
        pass
    # with self.assertRaises(TypeError):
    #     User.objects.create_user()
    # with self.assertRaises(TypeError):
    #     User.objects.create_user(email='')
    # with self.assertRaises(ValueError):
    #     User.objects.create_user(email='', password="foo")


@pytest.mark.django_db
def test_create_superuser():
    User = get_user_model()
    admin_user = User.objects.create_superuser('super@user.com', 'foo')

    assert admin_user.email == 'super@user.com'
    assert admin_user.is_active is True
    assert admin_user.is_staff is True
    assert admin_user.is_superuser is True
    try:
        # username is None for the AbstractUser option
        # username does not exist for the AbstractBaseUser option
        assert admin_user.username is None
    except AttributeError:
        pass
    # with self.assertRaises(ValueError):
    #     User.objects.create_superuser(
    #         email='super@user.com', password='foo', is_superuser=False)
