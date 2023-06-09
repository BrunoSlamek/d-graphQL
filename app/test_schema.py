import pytest
from django.test import Client

from .schema import schema


def test_hello_query():
    client = Client()
    query = '''
        query {
            types {
                id
                name
            }
        }
    '''
    response = client.post('/graphql', {'query': query})
    assert response.status_code == 200
    assert response.json() == {
        "data": {
            "types": [
              {
                "id": "5",
                "name": "test5"
              },
              {
                "id": "6",
                "name": "test6"
              }
            ]
        }
    }
