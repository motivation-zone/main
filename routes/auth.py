from aiohttp import web
from db_sevice.user import get_user
from aiohttp_session import get_session


routes = web.RouteTableDef()


def set_session(session, user_login):
    session['user'] = user_login


@routes.post('/login')
async def login_post(request):
    data = await request.json()
    user_login = data.get('login')
    user_password = data.get('password')
    if await get_user(user_login, user_password):
        session = await get_session(request)
        set_session(session, user_login)
        index_url = "/"
        raise web.HTTPFound(index_url)
    return web.json_response({'error': 'Invalid user data'}, status=401, content_type='application/json')


@routes.get('/login')
async def login_get(request):
    return web.json_response({'msg': 'Need to login'}, status=401, content_type='application/json')