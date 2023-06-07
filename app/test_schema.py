import pytest
from django.test import Client

from .schema import schema


def test_hello_query():
    client = Client()
    query = '''
        query {
            hello
        }
    '''
    response = client.post('/graphql', {'query': query})
    assert response.status_code == 200
    assert response.json() == {
        'data': {
            'hello': 'Hello World! GraphQL with Django!'
        }
    }