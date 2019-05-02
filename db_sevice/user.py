from fake_data.user import users


async def get_user(login: str, password: str) -> bool:
    return login in users and users[login] == password
