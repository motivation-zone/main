from db_sevice.helpers.requests import request_to_db_service, handle_response


class Sport:
    paths = {
        'get_sport_dy_user': 'sport/get-sports/{user_id}',
        'get_all': 'sport/get-sports',
        'user_add_sport': 'sport/update-user-sport/add',
        'user_delete_sport': 'sport/update-user-sport/delete',
        'get_users': 'sport/get-users/{sport_id}',
    }

    @staticmethod
    async def get_by_user(user_id):
        response = await request_to_db_service(
            {
                'type': 'GET',
                'url': Sport.paths['get_sport_dy_user'].format(user_id=user_id),
            }
        )

        status, data = await handle_response(response)
        if status == 200:
            return data
        return status

    @staticmethod
    async def get_all():
        response = await request_to_db_service(
            {
                'type': 'GET',
                'url': Sport.paths['get_all'],
            }
        )
        return await handle_response(response)

    @staticmethod
    async def add_sport(user_id, sport_id):
        response = await request_to_db_service(
            {
                'type': 'POST',
                'url': Sport.paths['user_add_sport'],
                'data': {
                    'userId': user_id,
                    'sportId': sport_id
                }
            }
        )
        return await handle_response(response)

    @staticmethod
    async def delete_sport(user_id, sport_id):
        response = await request_to_db_service(
            {
                'type': 'POST',
                'url': Sport.paths['user_delete_sport'],
                'data': {
                    'userId': user_id,
                    'sportId': sport_id
                }
            }
        )
        return await handle_response(response)

    @staticmethod
    async def delete_all_links(user_id):
        status, data = await Sport.get_all()
        if status != 200:
            return False
        for sport in data:
            response = await request_to_db_service(
                {
                    'type': 'POST',
                    'url': Sport.paths['user_delete_sport'],
                    'data': {
                        'userId': user_id,
                        'sportId': sport['id']
                    }
                }
            )
            status, data = await handle_response(response)
            if status != 200:
                return False
        return True

    @staticmethod
    async def get_users(sport_id):
        response = await request_to_db_service(
            {
                'type': 'GET',
                'url': Sport.paths['get_users'].format(sport_id=sport_id),
                'params': {'limit': 1_000_000, 'skip': 0}
            }
        )
        return await handle_response(response)

