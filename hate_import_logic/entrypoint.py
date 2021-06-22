from hate_import_logic.app import App
from hate_import_logic.webserver import WebServer


def main():
    pass


class Config:
    pass


def init_config() -> Config:
    """
    Reads config from APP_CONFIG env variable
    :return:
    """
    ...


def init_redis_from_config(config: Config) -> WebServer:
    ...

webserver_stop_signal = ...


if __name__ == '__main__':
    """
    Entrypoint is invoked as script on production to run app, that will be configured by YAML config in local
    filesystem
    """
    config = init_config()
    redis = init_redis_from_config(config)

    web_server = WebServer(redis)
    app = App(web_server)
    app.run()

    # We wait Ctrl+C to stop webserver
    while not webserver_stop_signal:
        sleep(1000)

    app.stop()

