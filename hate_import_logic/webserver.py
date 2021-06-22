from hate_import_logic.redis import Redis


def init_handlers():
    raise NotImplementedError


def router(route: str, method: str):
    raise NotImplementedError


class WebServer:

    def __init__(self, redis: Redis):
        self._redis = redis

    def run(self):
        pass

    def stop(self):
        pass

    @router("/invoice", "POST")
    def handle_post_invoice(self, request):
        self._redis.process(request)

    ...
