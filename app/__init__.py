from flask import Flask
from .routes import api
from .errors import register_error_handlers
def create_app():
    app = Flask(__name__)

# Register Blueprints
    app.register_blueprint(api, url_prefix='/api/v1')

# Register Error Handlers
    register_error_handlers(app)
    return app

 