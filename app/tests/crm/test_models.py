import pytest

from crm.models import CustomerNote


@pytest.mark.django_db
def test_create_image(add_image, get_user):
    user = get_user()
    image_file_object = add_image(name="dor_image", image_file_name="profile.jpg", user=user)

    image_file_object.tags.add("profile")

    assert image_file_object is not None
    assert image_file_object.title == "dor_image"
    assert image_file_object.file is not None
    assert "dor_image" in image_file_object.file.name
    assert "profile" in image_file_object.tags.names()


@pytest.mark.django_db
def test_create_customer(add_image, add_customer, get_user):
    user = get_user()

    customer_picture = add_image(
        name=f"dor_image",
        image_file_name="profile.jpg",
        user=user
    )
    customer = add_customer(
        name="Dor",
        user=user,
        customer_picture=customer_picture
    )

    assert customer.first_name == "Dor"
    assert customer.email == "dor.b4r@gmail.com"
    assert customer.phone == "+972502022337"
    assert int(customer.created_at.timestamp()) == int(
        customer.modified_at.timestamp()
    )


@pytest.mark.django_db
def test_create_customer_note(get_user, add_image, add_customer):
    user = get_user()

    customer_picture = add_image(
        name=f"dor_image",
        image_file_name="profile.jpg",
        user=user
    )
    customer = add_customer(
        name="Dor",
        user=user,
        customer_picture=customer_picture
    )

    customer_note = CustomerNote.objects.create(
        customer=customer,
        title="Note Title",
        body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
        "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type"
        "and scrambled it to make a type specimen book. It has survived not only five centuries, but also the"
        "leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s"
        "with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop"
        "publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    )

    assert customer_note is not None
    assert customer_note.title == "Note Title"
    assert len(customer_note.body) > 300
