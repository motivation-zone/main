from aiohttp import web
from routes_union import setup_routes
from aiohttp_session import session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp_session import SimpleCookieStorage
import hashlib
from settings import *
from middlewares.authorization import authorization


async def init_app(mode='prod'):
    middle = []
    if mode == 'test':
        middle.append(session_middleware(SimpleCookieStorage()))
    else:
        middle.append(session_middleware(EncryptedCookieStorage(hashlib.sha256(bytes(SECRET_KEY, 'utf-8')).digest())))

    middle.append(authorization)

    app = web.Application(
        middlewares=middle
    )
    setup_routes(app)

    return app


def main():
    app = init_app()
    web.run_app(app,
                host='127.0.0.1',
                port=8000)


if __name__ == '__main__':
    main()
