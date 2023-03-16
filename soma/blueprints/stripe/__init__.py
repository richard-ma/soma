from flask import Blueprint, render_template, redirect, url_for, request
from soma.models import db, Stripe
from soma.forms import CreateStripeForm


bp = Blueprint('stripe', __name__, url_prefix='/stripe', template_folder='templates')

@bp.route("/")
def index():
    return redirect(url_for("stripe.stripes"))

@bp.route("/stripes")
def stripes():
    stripes = db.session.execute(db.select(Stripe).order_by(Stripe.id.desc())).scalars()
    return render_template("stripe/list.html", stripes=stripes)

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
            status = 1 if request.form['status'] == 'y' else 0,
            beizhu = request.form['beizhu'],
            updatetime = 12333,
            scid = '',
            lcid = '',
            ssid = '',
            lsid = '',
            type = '0',
            sid = 0,
            lasttime = 12333,
            admin_id = 0,
            purl = request.form['purl']
        )

        db.session.add(stripe)
        db.session.commit()
        
        return redirect(url_for('stripe.index'))

    form = CreateStripeForm()
    return render_template("stripe/create.html", form=form)