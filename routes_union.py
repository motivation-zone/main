from routes.index import routes as index_routes


def setup_routes(app):
    app.add_routes(index_routes)
