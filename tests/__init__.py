import pytest

from hate_import_logic.app import App
from hate_import_logic.redis import Redis
from hate_import_logic.webserver import WebServer


@pytest.fixture()
def mock_redis() -> Redis:
    raise NotImplementedError


def run_in_background(app: App):
    raise NotImplementedError


def test_post_invoice(mock_redis):

    webserver = WebServer(mock_redis)
    app = App(webserver)
    app.start()
    run_in_background()
