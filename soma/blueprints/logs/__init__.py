from flask import Blueprint, render_template


bp = Blueprint('logs', __name__, url_prefix='/logs', template_folder='templates')

@bp.route("/")
def index():
    return render_template("logs/index.html")