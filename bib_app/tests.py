import pytest
from django.test import TestCase, Client as WebClient

# Create your tests here.
from django.urls import reverse


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_authors(client):
    url = reverse('authors')
    response = client.get(url)
    assert  response.status_code == 200
