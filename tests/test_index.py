from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from main import init_app
from models.user import User
from db_sevice.sport import Sport


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        return await init_app()

    @unittest_run_loop
    async def test_example(self):
        resp = await self.client.request("GET", "/")
        assert resp.status == 200
        json_resp = await resp.json()
        assert {'msg': 'OK'} == json_resp

    @unittest_run_loop
    async def test_example(self):
        data = await Sport.get_by_user('27eed8a9-5557-4b5e-9609-507c02406198')
