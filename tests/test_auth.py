from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from main import init_app
import json
from db_sevice.user import User as User_model


class AuthTestCase(AioHTTPTestCase):
    user_data = {
        'login': 'login',
        'name': 'user',
        'password': 'password',
        'email': 'your_mom@mail.ru',
        'gender': True
    }

    async def get_application(self):
        await User_model.remove_users()
        return await init_app(mode='test')

    @unittest_run_loop
    async def test_join(self):
        resp = await self.client.post("/join", json=self.user_data)
        assert resp.status == 200
        json_resp = await resp.json()
        assert {'status': 'OK'} == json_resp

    @unittest_run_loop
    async def test_login(self):
        # first create user
        await self.client.post("/join", json=self.user_data)
        resp = await self.client.post("/login", json={
            'login': self.user_data['login'],
            'password': self.user_data['password']
        })
        assert resp.status == 200
        json_resp = await resp.json()
        assert {'status': 'OK'} == json_resp

        user_from_cookies = json.loads(resp.cookies['AIOHTTP_SESSION'].value)['session']['user']
        assert self.user_data['login'] == user_from_cookies

    @unittest_run_loop
    async def test_logout(self):
        # first login
        await self.client.post("/login", json={
            'login': self.user_data['login'],
            'password': self.user_data['password']
        })

        resp = await self.client.get("/logout")
        assert resp.status == 200
        json_resp = await resp.json()
        assert {'status': 'OK'} == json_resp

        session_from_cookies = json.loads(resp.cookies['AIOHTTP_SESSION'].value)
        assert {} == session_from_cookies

    @unittest_run_loop
    async def test_logout_without_login(self):
        resp = await self.client.get("/logout")
        assert resp.status == 409
