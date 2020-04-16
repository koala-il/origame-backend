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
