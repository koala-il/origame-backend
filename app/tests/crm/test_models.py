import pytest

from crm.models import Customer


@pytest.mark.django_db
def test_create_image(add_image):
    # image_path = os.path.join(settings.BASE_DIR, 'tests', 'crm', 'assets', 'profile.jpg')
    # with open(image_path, 'rb') as image_file:
    #     image_uploaded_file = SimpleUploadedFile(
    #         name="dor_image",
    #         content=image_file.read(),
    #         content_type='image/jpeg'
    #     )
    #
    # image_file_object = ImageFile.objects.create(
    #     title="dor_image",
    #     file=image_uploaded_file,
    # )

    image_file_object = add_image(
        name="dor_image",
        image_file_name='profile.jpg'
    )

    image_file_object.tags.add("profile")

    assert image_file_object is not None
    assert image_file_object.title == "dor_image"
    assert image_file_object.file is not None
    assert "dor_image" in image_file_object.file.name
    assert "profile" in image_file_object.tags.names()


@pytest.mark.django_db
def test_create_customer(add_image):
    customer_picture = add_image(
        name="dor_image",
        image_file_name='profile.jpg'
    )

    customer = Customer.objects.create(
        first_name="Dor",
        last_name="Bar",
        address_line_1="Moshav Kanaf, Golan, 1293000",
        address_line_2="",
        city="Kanaf",
        state="Golan",
        country="Israel",
        picture=customer_picture,
        phone="+972502022337",
        email="dor.b4r@gmail.com",
        facebook="https://www.facebook.com/dor4231",
        instagram="https://www.instagram.com/dor4231/",
        twitter="https://twitter.com/dorb4r",
        created_date="normal@user.com",
        last_modify_date="normal@user.com",
    )

    assert customer.first_name == "Dor"
    assert customer.email == "dor.b4r@gmail.com"
    assert customer.phone == "+972502022337"
    assert int(customer.created_date.timestamp()) == int(customer.last_modify_date.timestamp())

    # except AttributeError:
    #     pass
    # with self.assertRaises(TypeError):
    #     User.objects.create_user()
    # with self.assertRaises(TypeError):
    #     User.objects.create_user(email='')
    # with self.assertRaises(ValueError):
    #     User.objects.create_user(email='', password="foo")

