import os
from flask import send_file

TEMPLATE_FOLDER = os.path.normpath(
    os.path.join(os.path.dirname(__file__), 'templates')
)


def send_static(filename):
    filepath = os.path.join(TEMPLATE_FOLDER, filename)
    return send_file(filepath)
