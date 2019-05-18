from db_sevice.user import User as User_model


class User:
    required_fields = {
        'login': True,
        'name': True,
        'password': True,
        'email': True,
        'gender': True,
    }
    optional_fields = {}

    @staticmethod
    def get_missing_fields(user_params: dict):
        missing_fields = []
        for field in User.required_fields.keys():
            if field not in user_params:
                missing_fields.append(field)

        return missing_fields

    @staticmethod
    async def create_user(user_params: dict):
        error_message = ''
        status = 409
        missing_fields = User.get_missing_fields(user_params)
        if not missing_fields:
            status, user_data = await User_model.create_user(user_params)
            if status == 200:
                return status, user_data[0]['id']
            else:
                error_message = user_data['message']
        else:
            error_message = 'Missing fields: ' + ', '.join(missing_fields)
        return status, error_message

    @staticmethod
    async def check_user(user_params: dict):
        return await User_model.check_user(user_params)

    @staticmethod
    async def update_user(user_login, user_params: dict):
        user = await User_model.get_user_by_login(user_login)
        if not user:
            return 404, "User not found"

        for parameter in user_params.keys():

            if parameter == 'id':  # нельзя давать редактировать id
                continue
            if user.get(parameter):
                user[parameter] = user_params[parameter]

        status, data = await User_model.update_user(user['id'], user_params)
        if status == 200:
            return status, 'OK'
        else:
            error_message = data['message']
        return status, error_message

    @staticmethod
    async def delete_user(user_id):
        status, data = await User_model.delete_user(user_id)
        if status == 200:
            return status, 'OK'
        else:
            error_message = data['message']
        return status, error_message
