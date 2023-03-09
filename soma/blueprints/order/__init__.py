from flask import Blueprint, render_template, url_for, redirect
from soma.models import db, Order


bp = Blueprint('order', __name__, url_prefix='/order', template_folder='templates')

@bp.route("/")
def index():
    return redirect(url_for("order.orders"))

@bp.route("/orders")
def orders():
    orders = db.session.execute(db.select(Order).order_by(Order.id)).scalars()
    return render_template("order/orders.html", orders=orders)