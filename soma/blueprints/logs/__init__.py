from flask import Blueprint, render_template, redirect, url_for
from soma.models import db, Log
from soma.helpers import *


bp = Blueprint('logs', __name__, url_prefix='/logs', template_folder='templates')

@bp.route("/")
def index():
    return redirect(url_for('logs.logs'))

@bp.route("/logs")
def logs():
    logs = db.session.execute(db.select(Log).order_by(Log.id.desc())).scalars()
    return render_template('logs/list.html', logs=logs)