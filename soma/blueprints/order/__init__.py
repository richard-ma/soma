from flask import Blueprint, render_template


bp = Blueprint('order', __name__, url_prefix='/order', template_folder='templates')

@bp.route("/")
def index():
    render_template("index.html")