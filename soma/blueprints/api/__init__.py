from flask import Blueprint, render_template


bp = Blueprint('api', __name__, url_prefix='/api', template_folder='templates')

@bp.route("/")
def index():
    return render_template("api/index.html")