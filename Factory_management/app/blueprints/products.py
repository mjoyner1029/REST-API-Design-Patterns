from flask import Blueprint, request, jsonify
from ..models import db, Product
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter

bp = Blueprint('products', __name__)
limiter = Limiter(key_func=get_remote_address)

@bp.route('', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limit
def create_product():
    data = request.json
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'id': new_product.id}), 201

@bp.route('', methods=['GET'])
@limiter.limit("10 per minute")  # Rate limit
def get_products():
    products = Product.query.all()
    return jsonify([{'id': prod.id, 'name': prod.name, 'price': prod.price} for prod in products])
