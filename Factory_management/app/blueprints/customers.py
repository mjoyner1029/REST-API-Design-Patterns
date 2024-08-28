from flask import Blueprint, request, jsonify
from ..models import db, Customer
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter

bp = Blueprint('customers', __name__)
limiter = Limiter(key_func=get_remote_address)

@bp.route('', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limit
def create_customer():
    data = request.json
    new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'id': new_customer.id}), 201

@bp.route('', methods=['GET'])
@limiter.limit("10 per minute")  # Rate limit
def get_customers():
    customers = Customer.query.all()
    return jsonify([{'id': cust.id, 'name': cust.name, 'email': cust.email, 'phone': cust.phone} for cust in customers])
