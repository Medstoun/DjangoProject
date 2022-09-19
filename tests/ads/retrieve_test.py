import pytest


@pytest.mark.django_db
def test_ad_retrieve(client, ad, user_token):
    expected_response = {
        "id": ad.id,
        "category": ad.category,
        "is_published": ad.is_published,
        "name": ad.name,
        "price": ad.price,
        "image": ad.image.url if ad.image else None,
        "description": ad.description,
        "author": ad.author.username
    }

    response = client.get(
        f'/ad/{ad.id}/',
        HTTP_AUTHORIZATION='Bearer ' + user_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
