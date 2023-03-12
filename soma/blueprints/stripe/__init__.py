from flask import Blueprint, render_template, redirect, url_for
from soma.models import db, Stripe


bp = Blueprint('stripe', __name__, url_prefix='/stripe', template_folder='templates')

@bp.route("/")
def index():
    return redirect(url_for("stripe.stripes"))

@bp.route("/stripes")
def stripes():
    stripes = db.session.execute(db.select(Stripe).order_by(Stripe.id)).scalars()
    return render_template("stripe/stripes.html", stripes=stripes)