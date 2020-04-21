import os

import pytest
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from crm.models import ImageFile, Customer


@pytest.fixture(scope="function")
def add_image():
    def _add_image(name, image_file_name):
        image_path = os.path.join(
            settings.BASE_DIR, "tests", "crm", "assets", image_file_name
        )
        with open(image_path, "rb") as image_file:
            image_uploaded_file = SimpleUploadedFile(
                name=name, content=image_file.read(), content_type="image/jpeg"
            )

        image_file_object = ImageFile.objects.create(
            title=name, file=image_uploaded_file,
        )
        return image_file_object

    return _add_image


@pytest.fixture(scope="function")
def add_customer():
    def _add_customer(name, customer_picture):
        customer = Customer.objects.create(
            first_name=name,
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
        )

        return customer

    return _add_customer
