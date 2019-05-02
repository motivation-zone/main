from aiohttp import web
from aiohttp.web import middleware
from aiohttp_session import get_session


@middleware
async def authorization(request, handler):
    print(request.path, request.method)

    def is_need_auth(path):
        return path not in ["/", '/login']

    session = await get_session(request)
    if session.get("user"):
        return await handler(request)
    elif is_need_auth(request.path):
        raise web.HTTPFound('/login')
    else:
        return await handler(request)
