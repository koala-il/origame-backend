import json

import pytest
from django.urls import reverse


@pytest.mark.db_django
def test_ping(client):
    url = reverse("request-ping")

    response = client.get(url)

    content = json.loads(response.content)

    assert response.status_code == 200
    assert content["ping"] == "pong!"


@pytest.mark.db_django
def test_version(client):
    url = reverse("request-app-version")

    response = client.get(url)

    content = json.loads(response.content)

    assert response.status_code == 200
    assert "version" in content
    assert isinstance(content["version"], str)
