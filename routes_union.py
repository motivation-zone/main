from routes.index import routes as index_routes
from routes.auth import routes as auth_routes
from routes.user_page import routes as user_page_routes


def setup_routes(app):
    app.add_routes(index_routes)
    app.add_routes(auth_routes)
    app.add_routes(user_page_routes)
