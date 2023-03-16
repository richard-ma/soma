from flask import Blueprint, render_template, redirect, url_for, request
from soma.models import db, Shop
from soma.forms import CreateShopForm


bp = Blueprint('shop', __name__, url_prefix='/shop', template_folder='templates')

@bp.route("/")
def index():
    return redirect(url_for("shop.shops"))

@bp.route("/shops")
def shops():
    shops = db.session.execute(db.select(Shop).order_by(Shop.id.desc())).scalars()
    return render_template("shop/list.html", shops=shops)

@bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        shop = Shop(
            url = request.form['url'],
            status = 1 if request.form['status'] == 'y' else 0,
            beizhu = request.form['beizhu'],
            sitegroup = 1,
            paypaltype = '1',
            paypalname = "paypal product",
            paypalname_me = '',
            donatename = '',
            updatetime = "123333",
            type = None,
            risk = None,
            admin_id = None,
        )

        db.session.add(shop)
        db.session.commit()

        return redirect(url_for("shop.index"))

    form = CreateShopForm()
    return render_template("shop/create.html", form=form)