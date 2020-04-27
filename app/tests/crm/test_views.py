import pytest
from django.test.client import Client
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from crm.models import Customer


@pytest.mark.django_db
def test_create_customer(client: Client, add_user, add_image):
    """
    Sanity add customer test
    """
    customers = Customer.objects.all()
    assert len(customers) == 0

    user = add_user(
        email="user@origame.com",
        password="Aa1234567"
    )

    profile_image = add_image(name="dor_image", image_file_name="profile.jpg", user=user)

    url = reverse("customers-view")

    jwt_token = RefreshToken.for_user(user)
    headers = {
        "HTTP_AUTHORIZATION": f"JWT {str(jwt_token.access_token)}"
    }

    response = client.post(
        url,
        data={
            "first_name": "Dor",
            "last_name": "Bar",
            "phone": "+972502022337",
            "email": "dor@bar.com",
            "country": "IL",
            "picture": profile_image.id
        },
        content_type="application/json",
        **headers
    )
    assert response.status_code == 201
    assert response.data["first_name"] == "Dor"
    assert response.data["last_name"] == "Bar"
    assert response.data["country"] == "IL"

    customers = Customer.objects.all()
    assert len(customers) == 1


@pytest.mark.django_db
def test_create_customer_no_authentication(client):
    customers = Customer.objects.all()
    assert len(customers) == 0

    url = reverse("customers-view")
    response = client.post(
        url,
        data={
            "first_name": "Dor",
            "last_name": "Bar",
            "phone": "+972502022337",
            "email": "dor@bar.com",
            "country": "IL"
        },
        content_type="application/json",
    )

    assert response.status_code == 401

    customers = Customer.objects.all()
    assert len(customers) == 0


@pytest.mark.django_db
def test_list_customers(client, add_customer, add_user, add_image):
    user = add_user(
        email="dor@dor.com",
        password="Aa1234567"
    )
    user_2 = add_user(
        email="ido@ido.com",
        password="Aa1234567"
    )

    customer_picture = add_image(name="dor_image", image_file_name="profile.jpg", user=user)
    customer_picture_other_user = add_image(name="dor_image", image_file_name="profile.jpg", user=user_2)

    add_customer(
        name="Dor",
        user=user,
        customer_picture=customer_picture
    )
    add_customer(
        name="Ido",
        user=user,
        customer_picture=customer_picture
    )
    add_customer(
        name="Danielle",
        user=user,
        customer_picture=customer_picture
    )
    add_customer(
        name="Dor",
        user=user_2,
        customer_picture=customer_picture_other_user
    )

    url = reverse("customers-view")

    jwt_token = RefreshToken.for_user(user)

    headers = {
        "HTTP_AUTHORIZATION": f"JWT {str(jwt_token.access_token)}"
    }

    response = client.get(
        url,
        content_type="application/json",
        **headers
    )

    assert response.status_code == 200
    assert len(response.data) == 3
