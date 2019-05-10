from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/api/index')
async def index(request):
    return web.json_response({'msg': 'OK'}, status=200, content_type='application/json')


@routes.post('/join_it')
async def index(request):
    return web.json_response({'msg': 'OK'}, status=200, content_type='application/json')
