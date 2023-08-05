from flask import Flask, jsonify, redirect
from .helpers import send_static
import werkzeug.exceptions as httperror

app = Flask(__name__)


@app.route('/')
def index():
    return send_static('index.html')


@app.route('/<path:path>')
def serve_file(path):
    try:
        return send_static(path)
    except httperror.NotFound as e:
        return send_static('index.html')


@app.route('/api/projects')
def projects_data():
    return str([])


@app.route('/api/<path:path>')
def api_404_handler(path):
    return jsonify({
        "message": "Route not found."
    }), 404


if __name__ == '__main__':
    app.run(debug=True)
