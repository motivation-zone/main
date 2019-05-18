from aiohttp import web
from models.user import User
from db_sevice.sport import Sport
from aiohttp_session import get_session


routes = web.RouteTableDef()


@routes.get('/user_page')
async def index(request):
    return web.json_response({'msg': 'OK'}, status=200, content_type='application/json')


@routes.post('/user/update')
async def update(request):
    session = await get_session(request)
    user_login = session.get('user', '')
    data = await request.json()
    status, data = await User.update_user(user_login, data)

    if status == 200:
        return web.json_response({'status': 'OK'}, status=status, content_type='application/json')
    else:
        return web.json_response({'error': data}, status=status, content_type='application/json')


@routes.get('/user/delete')
async def update(request):
    session = await get_session(request)
    user_id = session.get('user_id', '')
    status, data = await User.delete_user(user_id)

    if status == 200:
        return web.json_response({'status': 'OK'}, status=status, content_type='application/json')
    else:
        return web.json_response({'error': data}, status=status, content_type='application/json')

