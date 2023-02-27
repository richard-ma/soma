from flask import Blueprint, jsonify, request


bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route("/")
@bp.route("/ping")
def ping():
    return jsonify({
        'message': 'pong'
    })


@bp.route('/post_data_test', methods=['GET', 'POST'])
def post_data_test():
    return jsonify({
        'form': request.form,
        'json': request.json,
    })