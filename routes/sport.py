from aiohttp import web
from db_sevice.sport import Sport
from aiohttp_session import get_session
from db_sevice.helpers.list import field_in_list

routes = web.RouteTableDef()


@routes.post('/user/sport/add')
async def sport_add(request):
    session = await get_session(request)
    data = await request.json()
    sport_id = data.get('sport_id')
    status, sport_types = await Sport.get_all()
    if not isinstance(sport_types, list):
        return web.json_response({'error': 'Error with service'}, status=data, content_type='application/json')

    user_id = session.get('user_id', '')
    if field_in_list(sport_types, 'id', sport_id) and user_id:
        status, data = await Sport.add_sport(user_id, sport_id)
        if status == 200:
            return web.json_response({'data': data}, status=200, content_type='application/json')
        if status == 409:
            return web.json_response({'error': 'Link already exists'}, status=status, content_type='application/json')
    return web.json_response({'error': 'Error with service'}, status=status, content_type='application/json')


@routes.post('/user/sport/delete')
async def sport_delete(request):
    session = await get_session(request)
    data = await request.json()
    sport_id = data.get('sport_id')
    status, sport_types = await Sport.get_all()
    if not isinstance(sport_types, list):
        return web.json_response({'error': 'Error with service'}, status=data, content_type='application/json')

    user_id = session.get('user_id', '')
    if field_in_list(sport_types, 'id', sport_id) and user_id:
        status, data = await Sport.delete_sport(user_id, sport_id)
        if status == 200:
            return web.json_response({'data': data}, status=200, content_type='application/json')
    return web.json_response({'error': 'Error with service'}, status=status, content_type='application/json')


@routes.get('/user/sport')
async def get_user_sports(request):
    session = await get_session(request)
    user_id = session.get('user_id', '')
    data = await Sport.get_by_user(user_id)
    if isinstance(data, list):
        return web.json_response({'data': data}, status=200, content_type='application/json')
    return web.json_response({'error': 'Error with service'}, status=data, content_type='application/json')


@routes.get('/sports')
async def get_all_sports(request):
    status, data = await Sport.get_all()
    if isinstance(data, list):
        return web.json_response({'data': data}, status=200, content_type='application/json')
    return web.json_response({'error': 'Error with service'}, status=data, content_type='application/json')


@routes.get('/sport/{sport_id}/users')
async def get_sport_users(request):
    sport_id = request.match_info['sport_id']
    status, data = await Sport.get_users(sport_id)
    if status == 200:
        return web.json_response({'data': data}, status=200, content_type='application/json')
    return web.json_response({'error': data['message']}, status=status, content_type='application/json')
