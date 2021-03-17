from flask import Flask, request, abort, jsonify, render_template
from flask_cors import CORS

from models import setup_db

def create_app (test_config=None):
    # Create and configure the app 
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')

    @app.route('/')
    def landing_page():
        return render_template('pages/index.html')


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not Found'
        }), 404


    return app

app = create_app()

if __name__ == '__main__':
    app.run()