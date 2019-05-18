from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from main import init_app
import json
from db_sevice.user import User as User_model
from fake_data.user import user_data as fake_user


class UserTestCase(AioHTTPTestCase):
    user_data = fake_user

    async def get_application(self):
        return await init_app(mode='test')

    @unittest_run_loop
    async def test_update(self):
        # first create user
        await self.client.post("/join", json=self.user_data)
        # first login
        await self.client.post("/login", json={
            'login': self.user_data['login'],
            'password': self.user_data['password']
        })

        data_to_update = self.user_data
        data_to_update['weight'] = 100
        resp = await self.client.post("/user/update", json=data_to_update)
        assert resp.status == 200
        json_resp = await resp.json()
        assert {'status': 'OK'} == json_resp

    @unittest_run_loop
    async def test_update_bad(self):
        data_to_update = self.user_data
        data_to_update['weight'] = 100
        resp = await self.client.post("/user/update", json=data_to_update)
        assert resp.status == 401

    @unittest_run_loop
    async def test_delete_user(self):
        # join
        await self.client.post("/join", json=self.user_data)
        # login
        await self.client.post("/login", json={
            'login': self.user_data['login'],
            'password': self.user_data['password']
        })
        resp = await self.client.get("/user/delete")
        assert resp.status == 200



