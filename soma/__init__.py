from flask import Flask, redirect, url_for
from soma.blueprints import api, order, shop, logs, stripe


app = Flask(__name__)
app.register_blueprint(api.bp)
app.register_blueprint(order.bp)
app.register_blueprint(shop.bp)
app.register_blueprint(stripe.bp)
app.register_blueprint(logs.bp)

@app.route("/")
def index():
    return redirect(url_for('order.index'))