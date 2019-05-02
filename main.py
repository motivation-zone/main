from aiohttp import web
from routes_union import setup_routes
from aiohttp_session import session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
import hashlib
from settings import *
from middlewares.authorization import authorization


async def init_app():
    middle = [
        session_middleware(EncryptedCookieStorage(hashlib.sha256(bytes(SECRET_KEY, 'utf-8')).digest())),
        authorization,
    ]

    app = web.Application(middlewares=middle)
    setup_routes(app)
    # setup_middlewares(app)

    return app


def main():
    app = init_app()
    web.run_app(app,
                host='127.0.0.1',
                port=8080)


if __name__ == '__main__':
    main()
