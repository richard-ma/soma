from flask import Flask, redirect, url_for
from soma.blueprints import api, order, shop, logs, stripe
from soma.models import db, migrate

def create_app(config_filename=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://soma:qwerty1234@localhost/soma'
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api.bp)
    app.register_blueprint(order.bp)
    app.register_blueprint(shop.bp)
    app.register_blueprint(stripe.bp)
    app.register_blueprint(logs.bp)

    @app.route("/")
    def index():
        return redirect(url_for('order.index'))

    return app