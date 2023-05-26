from flask import Flask, redirect, url_for
from soma.blueprints import api, order, shop, logs, stripe, settings
from soma.models import db, migrate
import soma.helpers as helpers
import os
import sys
import logging
from werkzeug.utils import import_string

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

    # load configration
    cfg = import_string(cfg_name)()
    app.config.from_object(cfg)

    # add logging handler
    logging_filename  = app.config.get('LOGGING_FILENAME', e + '.log')
    rotating_file_handler = RotatingFileHandler(
        os.path.join(app.instance_path, logging_filename),
        maxBytes=app.config.get('LOGGING_FILE_MAX_BYTES', 1024*1024),
        backupCount=app.config.get('LOGGING_FILE_BACKUP_COUNT', 10),
    )
    # set logging format
    logging_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s'
    logging_formatter = logging.Formatter(logging_format)
    rotating_file_handler.setFormatter(logging_formatter)
    # add handler to logger
    # TODO if you use flask-sqlalchemy add it's logger to this list
    for logger in (app.logger, ):
        logger.addHandler(rotating_file_handler)
        logger.setLevel(log_level)

    # logging configurations
    app.logger.debug("Loading Configration: " + cfg_name)
    app.logger.debug("Configration loaded: " + str(cfg))

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