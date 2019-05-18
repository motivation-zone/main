from db_sevice.helpers.requests import request_to_db_service, handle_response


class User:
    paths = {
        'create_user': 'user/create',
        'check_user': 'user/check-user-password',
        'get_users': 'user/get-users',
        'remove_user': 'user/delete-user/{}',
        'get_user_by_login': 'user/get-user/login/{}',
        'update_user': 'user/update-user/{}',
        'delete_user': 'user/delete-user/{user_id}',
    }

    @staticmethod
    async def create_user(user_data):
        response = await request_to_db_service({'type': 'POST', 'url': User.paths['create_user'], 'data': user_data})
        return await handle_response(response)

    @staticmethod
    async def check_user(user_data) -> str:
        response = await request_to_db_service({'type': 'POST', 'url': User.paths['check_user'], 'data': user_data})
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
        if data:
            for user in data['data']:
                await request_to_db_service({
                    'type': 'DELETE',
                    'url': User.paths['remove_user'].format(user['id']),
                })

    @staticmethod
    async def get_user_by_login(login) -> dict:
        response = await request_to_db_service({'type': 'GET', 'url': User.paths['get_user_by_login'].format(login),
                                                'params': {'strict': 'true'}}, )
        status, data = await handle_response(response)
        if status == 200 and data:
            return data[0]
        return {}

    @staticmethod
    async def update_user(user_id, user_data):
        response = await request_to_db_service(
            {
                'type': 'POST',
                'url': User.paths['update_user'].format(user_id),
                'data': user_data
            })
        return await handle_response(response)

    @staticmethod
    async def delete_user(user_id):
        response = await request_to_db_service(
            {
                'type': 'DELETE',
                'url': User.paths['delete_user'].format(user_id=user_id),
            })
        return await handle_response(response)
