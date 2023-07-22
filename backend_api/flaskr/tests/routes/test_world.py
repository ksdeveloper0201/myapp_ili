import pytest
from flaskr.providers import WorldProvider


def test_get_city(client):

    # mocker.patch.object()
    response = client.get("/city")

    assert response.status_code == 200
    assert response.json == {"message": "Example response"}


def test_get_city_with_server_error(client, mocker):
    """server_error時
    Args:
        client (_type_): _description_
    """

    # mocker.patch.object()
    mocker.patch.object(WorldProvider, "fetch_world", side_effect=Exception)
    response = client.get("/city")

    assert response.status_code == 500


def test_get_city_with_not_found(client):
    """_summary_

    Args:
        client (_type_): _description_
    """
    response = client.get("/city")

    assert response.status_code == 403
