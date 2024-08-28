from flask import Blueprint, request, jsonify
from ..models import db, Order
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter

bp = Blueprint('orders', __name__)
limiter = Limiter(key_func=get_remote_address)

@bp.route('', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limit
def create_order():
    data = request.json
    new_order = Order(
        customer_id=data['customer_id'],
        product_id=data['product_id'],
        quantity=data['quantity'],
        total_price=data['total_price']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'id': new_order.id}), 201

@bp.route('', methods=['GET'])
@limiter.limit("10 per minute")  # Rate limit
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        'id': ord.id,
        'customer_id': ord.customer_id,
        'product_id': ord.product_id,
        'quantity': ord.quantity,
        'total_price': ord.total_price
    } for ord in orders])
