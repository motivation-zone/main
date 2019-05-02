from aiohttp import web
from routes_union import setup_routes


async def init_app():

    app = web.Application()
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
