import aiohttp
from settings import *
from db_sevice.helpers.url_tools import make_url


async def request_to_db_service(request_data):
    print(make_url(DB_SERVICE_URL, request_data['url']))
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        if request_data['type'] == 'POST':
            response = await session.post(make_url(DB_SERVICE_URL, request_data['url']), json=request_data['data'])
        else:
            response = await session.request(request_data['type'],
                                             url=make_url(DB_SERVICE_URL, request_data['url']),
                                             params=request_data.get('params'))
    return response


async def handle_response(response):
    status = response.status
    response_data = await response.json()
    if status == 200:
        return status, response_data['data']
    else:
        return status, response_data['error']

