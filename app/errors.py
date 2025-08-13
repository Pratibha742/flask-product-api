from flask import jsonify


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Resource not found"}), 404
    
    @app.errorhandler(500)
    def interna_error(e):
        return jsonify({"error": "Internal server Error"}), 500