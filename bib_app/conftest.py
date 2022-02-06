import pytest
from django.test import Client as WebClient

from bib_app.models import Author


@pytest.fixture
def client():
    client = WebClient()
    return client


@pytest.fixture
def authors():
    lst = []
    a = Author.objects.create(first_name='slawek', last_name='bo')
    lst.append(a)
    a = Author.objects.create(first_name='Gosia', last_name='bo')
    lst.append(a)
    a = Author.objects.create(first_name='Kasia', last_name='bo')
    lst.append(a)
    return lst