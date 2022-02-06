import pytest
from django.test import TestCase, Client as WebClient

# Create your tests here.
from django.urls import reverse

from bib_app.models import Author, Book, Publisher


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
        'first_name': 'slawek',
        'last_name': 'Bo'
    }
    url = reverse('add_authors')
    response = client.post(url, dct)
    assert Author.objects.get(**dct)  # -> Author.objects.get(first_name='slawek',last_name='Bo')


@pytest.mark.django_db
def test_add_book(client, author):
    dct = {
        'title': 'HobsaaHobsaa',
        'author': str(author.id),
    }
    url = reverse('add_book')
    response = client.post(url, dct)
    assert Book.objects.first()


@pytest.mark.django_db
def test_login_view(client, user):
    dct= {
        'username':'gamon',
        'password':'ala'
    }
    url = reverse('login')
    response = client.post(url, dct)
    assert response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_publisher_add_view_without_login(client):
    url = reverse('add_publisher')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_publisher_add_view_without_login(user, client):
    url = reverse('add_publisher')
    client.force_login(user)
    dtc ={
        'name':'ala',
        'year':1999
    }
    client.post(url, dtc)
    assert Publisher.objects.get(**dtc)





