from flask import Flask, redirect, url_for
from soma.blueprints import order


app = Flask(__name__)
app.register_blueprint(order.bp)

@app.route("/")
def index():
    return redirect(url_for('order.index'))