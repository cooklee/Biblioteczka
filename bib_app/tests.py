import pytest
from django.test import TestCase, Client as WebClient

# Create your tests here.
from django.urls import reverse

from bib_app.models import Author


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_authors(client, authors):
    url = reverse('authors')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context['authors'].count() == len(authors)
    for item in authors:
        assert item in context['authors']


@pytest.mark.django_db
def test_add_author(client):
    dct = {
        'first_name':'slawek',
        'last_name':'Bo'
    }
    url = reverse('add_authors')
    response = client.post(url, dct)
    assert Author.objects.get(**dct) #-> Author.objects.get(first_name='slawek',last_name='Bo')




