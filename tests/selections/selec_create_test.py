import pytest


@pytest.mark.django_db
def test_create_selection(client, ad, user_token):
    expected_response = {
        "id": 1,
        "name": "test selection",
        "owner": ad.author.id,
        "items": [ad.id]
    }

    data = {
        'name': 'test selection',
        'owner': ad.author.id,
        'items': [ad.id],
    }

    response = client.post(
        '/selection/create/',
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION='Bearer ' + user_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
