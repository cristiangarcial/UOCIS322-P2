"""
Cristian Garcia Leon's Flask API.
"""
import config
import os
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

options = config.configuration()
DOCROOT = options.DOCROOT

@app.route("/path:page")
def hello(page):
    options = get_options()
    DOCROOT = options.DOCROOT
    return "UOCIS docker demo!\n"

@app.errorhandler(404)
def not_found(e):
    return send_from_directory('templates', '404.html'), 404

@app.errorhandler(403)
def forbidden:
    return send_from_directory('templates', '403.html'), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
