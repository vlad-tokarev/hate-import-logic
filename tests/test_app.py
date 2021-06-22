import pytest

from hate_import_logic.app import App
from hate_import_logic.redis import Redis
from hate_import_logic.webserver import WebServer


@pytest.fixture()
def mock_redis() -> Redis:
    raise NotImplementedError



class AppHttpClient:
    ...

def test_post_invoice(mock_redis):

    webserver = WebServer(mock_redis)
    app = App(webserver)
    app.start()

    client = AppHttpClient()
    response = client.post("/invoice", "POST", {"some": "example"})
    assert response.status_code == 200
    app.stop()