from pytest import fixture
from app_factory import create_app


@fixture
def app():
    app = create_app()
    yield app


@fixture
def client(app):
    return app.test_client()
