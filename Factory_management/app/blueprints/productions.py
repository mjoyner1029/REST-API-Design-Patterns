from flask import Blueprint, request, jsonify
from ..models import db, Production
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter

bp = Blueprint('productions', __name__)
limiter = Limiter(key_func=get_remote_address)

@bp.route('', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limit
def create_production():
    data = request.json
    new_production = Production(
        product_id=data['product_id'],
        quantity_produced=data['quantity_produced'],
        date_produced=data['date_produced']
    )
    db.session.add(new_production)
    db.session.commit()
    return jsonify({'id': new_production.id}), 201

@bp.route('', methods=['GET'])
@limiter.limit("10 per minute")  # Rate limit
def get_productions():
    productions = Production.query.all()
    return jsonify([{
        'id': prod.id,
        'product_id': prod.product_id,
        'quantity_produced': prod.quantity_produced,
        'date_produced': prod.date_produced.isoformat()
    } for prod in productions])
