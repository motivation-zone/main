from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from main import init_app
from fake_data.user import user_data as fake_user
from db_sevice.sport import Sport as Service_sport
from db_sevice.user import User as Service_user


class SportTestCase(AioHTTPTestCase):
    user_data = fake_user

    async def get_application(self):
        app = await init_app(mode='test')
        return app

    @unittest_run_loop
    async def test_user_sport(self):
        # first login
        await self.client.post("/login", json={
            'login': self.user_data['login'],
            'password': self.user_data['password']
        })

        data_to_update = self.user_data
        data_to_update['weight'] = 100
        resp = await self.client.get("/user/sport")
        assert resp.status == 200
        json_resp = await resp.json()
        assert {'data': []} == json_resp

    @unittest_run_loop
    async def test_get_sport(self):
        # first login
        await self.client.post("/login", json={
            'login': self.user_data['login'],
            'password': self.user_data['password']
        })

        resp = await self.client.get("/sports")
        assert resp.status == 200
        json_resp = await resp.json()
        assert len(json_resp) > 0

    @unittest_run_loop
    async def test_add_sport(self):
        # first create user
        await self.client.post("/join", json=self.user_data)
        # first login
        await self.client.post("/login", json={
            'login': self.user_data['login'],
            'password': self.user_data['password']
        })
        user = await Service_user.get_user_by_login(self.user_data['login'])
        status = await Service_sport.delete_all_links(user['id'])
        assert status
        sport_id = '2'
        resp = await self.client.post("/user/sport/add", json={'sport_id': sport_id})
        assert resp.status == 200
        json_resp = await resp.json()
        assert len(json_resp['data']) == 1
        assert json_resp['data'][0]['sportId'] == sport_id

    @unittest_run_loop
    async def test_get_users(self):
        # first create user
        await self.client.post("/join", json=self.user_data)
        # first login
        await self.client.post("/login", json={
            'login': self.user_data['login'],
            'password': self.user_data['password']
        })
        sport_id = '2'
        resp = await self.client.get("/sport/{}/users".format(sport_id))
        assert resp.status == 200
        json_resp = await resp.json()

    @unittest_run_loop
    async def test_delete_sport(self):
        # first login
        await self.client.post("/login", json={
            'login': self.user_data['login'],
            'password': self.user_data['password']
        })
        sport_id = '2'
        # first add link
        await self.client.post("/user/sport/add", json={'sport_id': sport_id})

        resp = await self.client.post("/user/sport/delete", json={'sport_id': sport_id})
        assert resp.status == 200
        json_resp = await resp.json()
        assert len(json_resp['data']) == 1
        assert json_resp['data'][0]['sportId'] == sport_id





