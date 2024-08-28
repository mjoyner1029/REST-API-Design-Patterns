from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
limiter = Limiter()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)

    from .blueprints import employees_bp, products_bp, orders_bp, customers_bp, productions_bp

    app.register_blueprint(employees_bp, url_prefix='/api/employees')
    app.register_blueprint(products_bp, url_prefix='/api/products')
    app.register_blueprint(orders_bp, url_prefix='/api/orders')
    app.register_blueprint(customers_bp, url_prefix='/api/customers')
    app.register_blueprint(productions_bp, url_prefix='/api/productions')

    return app
