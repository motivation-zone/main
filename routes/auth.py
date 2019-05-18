from aiohttp import web
# from db_sevice.user import get_user
from aiohttp_session import get_session
from models.user import User
from db_sevice.user import User as Service_user

routes = web.RouteTableDef()


def set_session(session, user_login, user_id):
    session['user'] = user_login
    session['user_id'] = user_id


@routes.post('/login')
async def login(request):
    data = await request.json()
    user_login = data.get('login')
    if await User.check_user(data):
        session = await get_session(request)
        user = await Service_user.get_user_by_login(user_login)
        if user:
            set_session(session, user_login, user['id'])
        return web.json_response({'status': 'OK'}, status=200, content_type='application/json')
    return web.json_response({'error': 'Invalid user data'}, status=401, content_type='application/json')


@routes.post('/join')
async def join(request):
    data = await request.json()
    status, data = await User.create_user(data)

    if status == 200:
        return web.json_response({'status': 'OK'}, status=status, content_type='application/json')
    else:
        return web.json_response({'error': data}, status=status, content_type='application/json')


@routes.get('/logout')
async def login(request):
    session = await get_session(request)
    if session.get('user'):
        del session['user']
        del session['user_id']
        return web.json_response({'status': 'OK'}, status=200, content_type='application/json')
    else:
        return web.json_response({'error': ''}, status=409, content_type='application/json')