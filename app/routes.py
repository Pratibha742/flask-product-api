from flask import Blueprint, request, jsonify
from .models import products
from .auth import require_auth
from .utils import paginate, filter_by_price

api = Blueprint('api',__name__)

@api.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@api.route("/products", methods =["GET"])
def get_products():
    limit = int(request.args.get("limit", len(products)))
    min_price = int(request.args.get("min_price",0))
    filtered = filter_by_price(products, min_price)
    return jsonify(paginate(filtered, limit))

@api.route("/products/<int:pid>", methods=["GET"])
def get_product(pid):
    for p in products:
        if p["id"] == pid:
            return jsonify(p)
    return jsonify({"error":"Not Found"}), 404
    
@api.route("/products", methods=["POST"])
@require_auth
def add_product():
    data = request.get_json()
    data["id"] = len(products) + 1
    products.append(data)
    return jsonify(data), 201


