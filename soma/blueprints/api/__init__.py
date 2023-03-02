from flask import Blueprint, jsonify, request


bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route("/")
@bp.route("/ping")
def ping():
    return jsonify({
        'message': 'pong'
    })

@bp.route('/post_json_test', methods=['GET', 'POST'])
def post_data_test():
    return jsonify(request.json)

@bp.route('post_form_test', methods=['GET', 'POST'])
def post_form_test():
    return jsonify(request.form)

@bp.route('/stripe', methods=['POST'])
def stripe_payment():
    data = request.form
    return jsonify(data)