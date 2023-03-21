from flask import Blueprint, render_template, redirect, url_for, request
from soma.models import db, Stripe
from soma.forms import CreateStripeForm
from soma.helpers import *


bp = Blueprint('stripe', __name__, url_prefix='/stripe', template_folder='templates')

@bp.route("/")
def index():
    return redirect(url_for("stripe.stripes"))

@bp.route("/stripes")
def stripes():
    stripes = db.session.execute(db.select(Stripe).order_by(Stripe.id.desc())).scalars()
    return render_template("stripe/list.html", stripes=stripes)

@bp.route("/enable/<int:id>")
def enable(id):
    stripe = db.get_or_404(Stripe, id)
    stripe.status = True
    db.session.commit()
    return redirect(url_for("stripe.index"))

@bp.route("/disable/<int:id>")
def disable(id):
    stripe = db.get_or_404(Stripe, id)
    stripe.status = False
    db.session.commit()
    return redirect(url_for("stripe.index"))

@bp.route("/delete/<int:id>")
def delete(id):
    stripe = db.get_or_404(Stripe, id)
    db.session.delete(stripe)
    db.session.commit()
    return redirect(url_for("stripe.index"))

@bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        stripe = Stripe(
            url = '',
            email = request.form['email'],
            mode = '0',
            pays = '1',
            limitway = '1',
            onemin = request.form['onemin'],
            onemax = request.form['onemax'],
            totalmoney = request.form['totalmoney'],
            totalnum = request.form['totalnum'],
            status = 1 if 'status' in request.form.keys() else 0,
            beizhu = request.form['beizhu'],
            updatetime = helper_datetime_to_timestamp(datetime.now()),
            scid = '',
            lcid = '',
            ssid = '',
            lsid = '',
            type = '0',
            sid = 0,
            lasttime = helper_datetime_to_timestamp(datetime.now()),
            admin_id = 0,
            purl = request.form['purl']
        )

        db.session.add(stripe)
        db.session.commit()
        
        return redirect(url_for('stripe.index'))

    form = CreateStripeForm()
    return render_template("stripe/create.html", form=form)