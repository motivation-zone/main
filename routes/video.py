from aiohttp import web
from multidict import MultiDict
import os
# from db_sevice.user import get_user
from aiohttp_session import get_session
from models.user import User

routes = web.RouteTableDef()


@routes.get('/video')
async def get(request):

    content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
     <form action="/video" method="post" accept-charset="utf-8"
      enctype="multipart/form-data">

    <label for="mp3">Mp3</label>
    <input id="mp3" name="mp3" type="file" value=""/>

    <input type="submit" value="submit"/>
    </form>
</body>
</html>'''
    return web.Response(text=content, content_type='text/html')


@routes.post('/video')
async def store_mp3_handler(request):
    reader = await request.multipart()

    # /!\ Don't forget to validate your inputs /!\

    # reader.next() will `yield` the fields of your form

    field = await reader.next()
    assert field.name == 'mp3'
    filename = field.filename
    # You cannot rely on Content-Length if transfer is chunked.
    size = 0
    with open(os.path.join('/Users/i-gataullin/GitHub/main/src', filename), 'wb') as f:
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)

    return web.Response(text='{} sized of {} successfully stored'
                             ''.format(filename, size))