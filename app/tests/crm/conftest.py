import os

import pytest
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from crm.models import ImageFile


@pytest.fixture(scope="function")
def add_image():
    def _add_image(name, image_file_name):
        image_path = os.path.join(settings.BASE_DIR, 'tests', 'crm', 'assets', image_file_name)
        with open(image_path, 'rb') as image_file:
            image_uploaded_file = SimpleUploadedFile(
                name=name,
                content=image_file.read(),
                content_type='image/jpeg'
            )

        image_file_object = ImageFile.objects.create(
            title=name,
            file=image_uploaded_file,
        )
        return image_file_object

    return _add_image
