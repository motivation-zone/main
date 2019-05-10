from fake_data.user import users
from db_sevice.helpers.requests import request_to_db_service, handle_response


class User:

    paths = {
        'create_user': 'user/create',
        'check_user': 'user/check-user-password',
        'get_users': 'user/get-users',
        'remove_user': 'user/delete-user/{}',
    }

    @staticmethod
    async def create_user(user_data):
        response = await request_to_db_service({'type': 'POST', 'url': User.paths['create_user'], 'data': user_data})
        return await handle_response(response)

    @staticmethod
    async def check_user(user_data) -> str:
        response = await request_to_db_service({'type': 'POST', 'url': User.paths['check_user'], 'data': user_data })
        if response.status == 200:
            return user_data['login']
        return ''

    @staticmethod
    async def remove_users():
        response = await request_to_db_service(
            {
                'type': 'GET',
                'url': User.paths['get_users'],
                'params': {'limit': 1_000_000, 'skip': 0}
            }
        )
        data = await response.json()
        for user in data['data']:
            await request_to_db_service({
                'type': 'DELETE',
                'url': User.paths['remove_user'].format(user['id']),
            })



