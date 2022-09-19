import pytest


@pytest.mark.django_db
def test_create_ad(client, user):
    expected_response = {
        "id": 1,
        "category": None,
        "is_published": False,
        "name": 'name name name',
        "price": 10,
        "description": None,
        "author": user.id
    }

    data = {
        "is_published": False,
        "name": 'name name name',
        "price": 10,
        "author": user.id
    }

    response = client.post(
        '/ad/create/',
        data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response
