from itertools import chain

from flask import Flask
from werkzeug.exceptions import NotFound, MethodNotAllowed, InternalServerError

from nidhoggr.bl import BaseUserRepo, BLConfig, BaseTextureRepo
from nidhoggr.views import auth, session, core


def configure_error_handlers(app: Flask):
    app.register_error_handler(NotFound, core.not_found)
    app.register_error_handler(MethodNotAllowed, core.method_not_allowed)
    app.register_error_handler(InternalServerError, core.internal_server_error)


def configure_views(app: Flask):
    for func in chain(auth.__all__, session.__all__):
        app.add_url_rule(f"/{func.__name__}", func.__name__, func, methods=["POST"])


def create_app(users: BaseUserRepo, config: BLConfig, textures: BaseTextureRepo) -> Flask:
    app = Flask(__package__)
    app.bl = {
        BaseUserRepo: users,
        BLConfig: config,
        BaseTextureRepo: textures
    }
    configure_error_handlers(app)
    configure_views(app)
    return app
