from flask import Flask, redirect, url_for, request

def create_app(config_filename=None):
    app = Flask(__name__)

    @app.route("/")
    def index():
        print("Server for A")
        return 'Server for A'

    @app.route('/api/stripe/', methods=['GET', 'POST'])
    def stripe_payment():
        print("/api/stripe")
        with open("api_stripe", 'w+') as f:
            f.write(str(request.form))
        print(request.form)
        return request.form

    return app