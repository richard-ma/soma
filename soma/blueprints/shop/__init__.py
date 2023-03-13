from flask import Blueprint, render_template, redirect, url_for
from soma.models import db, Shop


bp = Blueprint('shop', __name__, url_prefix='/shop', template_folder='templates')

@bp.route("/")
def index():
    return redirect(url_for("shop.shops"))

@bp.route("/shops")
def shops():
    shops = db.session.execute(db.select(Shop).order_by(Shop.id.desc())).scalars()
    return render_template("shop/list.html", shops=shops)