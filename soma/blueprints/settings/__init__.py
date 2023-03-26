from flask import Blueprint, render_template, url_for, redirect, request
from soma.models import db, Currency
from soma.forms import CreateCurrencyForm


bp = Blueprint('settings', __name__, url_prefix='/settings', template_folder='templates')

@bp.route("/")
def index():
    return redirect(url_for("settings.currency_currencies"))

@bp.route("/currency/currencies")
def currency_currencies():
    currencies = db.session.execute(db.select(Currency).order_by(Currency.code.desc())).scalars()
    return render_template("settings/currency/currencies.html", currencies=currencies)

@bp.route("/currency/delete/<string:code>")
def currency_delete(code):
    currency = db.get_or_404(Currency, code)
    db.session.delete(currency)
    db.session.commit()
    return redirect(url_for("settings.currency_currencies"))

@bp.route("/currency/create", methods=['GET', 'POST'])
def currency_create():
    if request.method == 'POST':
        currency = Currency(
            name = request.form.get('name', ''),
            code = request.form.get('code', '').upper(),
            value = float(request.form.get('value', '1.00')) # TODO add requeired validator
        )
        
        db.session.add(currency)
        db.session.commit()

        return redirect(url_for("settings.currency_currencies"))
    
    form = CreateCurrencyForm()
    return render_template("settings/currency/create.html", form=form)