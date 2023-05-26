from flask import Flask, redirect, url_for
from soma.blueprints import api, order, shop, logs, stripe, settings
from soma.models import db, migrate
import soma.helpers as helpers
import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)

def create_app(config_filename=None):
    app = Flask(__name__)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass # instance folder exists

    # get flask environment variable
    e = os.environ.get('FLASK_ENV', 'production') # default flask environment is production

    # set running mode
    if e == 'dev':
        cfg_name = 'config.DevelopmentConfig'
        log_level = logging.DEBUG
    elif e == 'testing':
        cfg_name = 'config.TestingConfig'
        log_level = logging.DEBUG
    else: # production as default
        cfg_name = 'config.ProductionConfig'
        log_level = logging.WARNING

    # app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://soma:qwerty1234@localhost/soma' # mysqlclient
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///soma.db' # sqlite3

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api.bp)
    app.register_blueprint(order.bp)
    app.register_blueprint(shop.bp)
    app.register_blueprint(stripe.bp)
    app.register_blueprint(logs.bp)
    app.register_blueprint(settings.bp)

    @app.route("/")
    def index():
        return redirect(url_for('order.index'))
    
    # template filter
    @app.template_filter('timestamp_to_datetime')
    def timestamp_to_datetime(s):
        return helpers.timestamp_to_datetime(s)

    @app.template_filter('status_display')
    def status_display(s):
        return helpers.status_display(s)

    return app