from flask import Blueprint, render_template, url_for, redirect
from soma.models import db, Currency


bp = Blueprint('settings', __name__, url_prefix='/settings', template_folder='templates')

@bp.route("/")
def index():
    return redirect(url_for("settings.orders"))

@bp.route("/currencies")
def currencies():
    currencies = db.session.execute(db.select(Currency).order_by(Currency.id.desc())).scalars()
    return render_template("settings/currencies.html", currencies=currencies)