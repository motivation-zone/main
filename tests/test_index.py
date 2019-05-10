from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from main import init_app


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        return await init_app()

    @unittest_run_loop
    async def test_example(self):
        resp = await self.client.request("GET", "/api/index")
        assert resp.status == 200
        json_resp = await resp.json()
        assert {'msg': 'OK'} == json_resp
