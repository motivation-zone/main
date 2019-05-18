from aiohttp import web
from aiohttp.web import middleware
from aiohttp_session import get_session


@middleware
async def authorization(request, handler):

    def is_need_auth(path):
        return path not in ["/", '/login', '/join', '/video']

    session = await get_session(request)
    if session.get("user"):
        return await handler(request)
    elif is_need_auth(request.path):
        return web.json_response(status=401)
    else:
        return await handler(request)
