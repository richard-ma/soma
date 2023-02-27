from flask import Blueprint, jsonify


bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route("/")
def index():
    return jsonify({
        'name': 'hello',
        'gender': 'world'
    })