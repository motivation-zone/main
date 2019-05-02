from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web
from main import init_app


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        return await init_app()

    @unittest_run_loop
    async def test_example(self):
        resp = await self.client.request("GET", "/")
        assert resp.status == 200
        text = await resp.text()
        assert "Hello, world" in text
