from flask import Blueprint, render_template


bp = Blueprint('stripe', __name__, url_prefix='/stripe', template_folder='templates')

@bp.route("/")
def index():
    return render_template("stripe/index.html")