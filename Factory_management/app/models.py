from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Employee id={self.id} name={self.name} position={self.position}>'

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    # Relationship with Order
    orders = db.relationship('Order', backref='product', lazy=True)
    # Relationship with Production
    productions = db.relationship('Production', backref='product', lazy=True)

    def __repr__(self):
        return f'<Product id={self.id} name={self.name} price={self.price}>'

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    
    # Relationship with Customer
    customer = db.relationship('Customer', backref='orders', lazy=True)
    # Relationship with Product
    product = db.relationship('Product', backref='orders', lazy=True)

    def __repr__(self):
        return f'<Order id={self.id} customer_id={self.customer_id} product_id={self.product_id} quantity={self.quantity} total_price={self.total_price}>'

class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    
    # Relationship with Order
    orders = db.relationship('Order', backref='customer', lazy=True)

    def __repr__(self):
        return f'<Customer id={self.id} name={self.name} email={self.email} phone={self.phone}>'

class Production(db.Model):
    __tablename__ = 'production'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity_produced = db.Column(db.Integer, nullable=False)
    date_produced = db.Column(db.Date, nullable=False)

    # Relationship with Product
    product = db.relationship('Product', backref='productions', lazy=True)

    def __repr__(self):
        return f'<Production id={self.id} product_id={self.product_id} quantity_produced={self.quantity_produced} date_produced={self.date_produced}>'
