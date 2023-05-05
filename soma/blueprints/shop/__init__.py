from flask import Blueprint, render_template, redirect, url_for, request
from soma.models import db, Shop
from soma.forms import CreateShopForm
import soma.helpers as helpers
from datetime import datetime


bp = Blueprint('shop', __name__, url_prefix='/shop', template_folder='templates')

@bp.route("/")
def index():
    return redirect(url_for("shop.shops"))

@bp.route("/shops")
def shops():
    shops = db.session.execute(db.select(Shop).order_by(Shop.id.desc())).scalars()
    return render_template("shop/list.html", shops=shops)

@bp.route("/enable/<int:id>")
def enable(id):
    shop = db.get_or_404(Shop, id)
    shop.status = True
    db.session.commit()
    return redirect(url_for("shop.index"))

@bp.route("/disable/<int:id>")
def disable(id):
    shop = db.get_or_404(Shop, id)
    shop.status = False
    db.session.commit()
    return redirect(url_for("shop.index"))

@bp.route("/delete/<int:id>")
def delete(id):
    shop = db.get_or_404(Shop, id)
    db.session.delete(shop)
    db.session.commit()
    return redirect(url_for("shop.index"))

@bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        shop = Shop(
            url = request.form['url'],
            status = 1 if 'status' in request.form.keys()  else 0,
            beizhu = request.form['beizhu'],
            sitegroup = 1,
            paypaltype = '1',
            paypalname = "paypal product",
            paypalname_me = '',
            donatename = '',
            updatetime = helpers.datetime_to_timestamp(datetime.now()),
            type = None,
            risk = None,
            admin_id = None,
        )

        shop.apikey = helpers.generate_api_key(shop.url)

        db.session.add(shop)
        db.session.commit()

        return redirect(url_for("shop.index"))

    form = CreateShopForm()
    return render_template("shop/create.html", form=form)