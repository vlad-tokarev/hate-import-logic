from hate_import_logic.webserver import WebServer


class App:

    def __init__(self, webserver: WebServer):
        self._webserver = webserver

    def run(self):
        self._webserver.run()

    def stop(self):
        self._webserver.stop()