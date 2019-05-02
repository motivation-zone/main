from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/user_page')
async def index(request):
    return web.json_response({'msg': 'OK'}, status=200, content_type='application/json')
