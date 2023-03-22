from flask import Blueprint, render_template, url_for, redirect, request
from soma.models import db, Currency
from soma.forms import CreateCurrencyForm


bp = Blueprint('settings', __name__, url_prefix='/settings', template_folder='templates')

@bp.route("/")
def index():
    return redirect(url_for("settings.currency_currencies"))

@bp.route("/currency/currencies")
def currency_currencies():
    currencies = db.session.execute(db.select(Currency).order_by(Currency.id.desc())).scalars()
    return render_template("settings/currency/currencies.html", currencies=currencies)

@bp.route("/currency/delete/<int:id>")
def currency_delete(id):
    currency = db.get_or_404(Currency, id)
    db.session.delete(currency)
    db.session.commit()
    return redirect(url_for("settings.currency_currencies"))

@bp.route("/currency/create", methods=['GET', 'POST'])
def currency_create():
    if request.method == 'POST':
        currency = Currency(
            name = request.form.get('name', ''),
            code = request.form.get('code', '').upper(),
            value = float(request.form.get('value', 0.00))
        )
        
        db.session.add(currency)
        db.session.commit()

        return redirect(url_for("settings.currency_currencies"))
    
    form = CreateCurrencyForm()
    return render_template("settings/currency/create.html", form=form)