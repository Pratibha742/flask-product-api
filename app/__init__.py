from flask import Flask
from .routes import api
from .errors import register_error_handlers
def create_app():
    app = Flask(__name__)

# Register Blueprints
    app.register_blueprint(api, url_prefix='/api/v1')

    # Root route (home)
    @app.route("/")
    def home():
        return {
            "message": "Welcome to the Flask Product API",
            "documentation": "Visit /api/v1 to access the API endpoints",
            "postman_collection": "https://github.com/Pratibha742/flask-product-api/raw/main/flask_products_api.postman_collection.json"
        }


# Register Error Handlers
    register_error_handlers(app)
    return app

 