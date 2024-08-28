from flask import Blueprint, request, jsonify
from ..models import db, Employee
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter

bp = Blueprint('employees', __name__)
limiter = Limiter(key_func=get_remote_address)

@bp.route('', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limit
def create_employee():
    data = request.json
    new_employee = Employee(name=data['name'], position=data['position'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'id': new_employee.id}), 201

@bp.route('', methods=['GET'])
@limiter.limit("10 per minute")  # Rate limit
def get_employees():
    employees = Employee.query.all()
    return jsonify([{'id': emp.id, 'name': emp.name, 'position': emp.position} for emp in employees])
