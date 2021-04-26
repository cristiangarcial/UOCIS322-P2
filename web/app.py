"""
Cristian Garcia Leon's Flask API.
"""
import config
import os
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

options = config.configuration()
DOCROOT = options.DOCROOT

@app.route("/<path:site>")
def hello(site):
    options = get_options()
    DOCROOT = options.DOCROOT
    if "~" in site or ".." in site or "//" in site:
        abort(403)
    elif site not int os.listdir(DOCROOT):
        abort(404)
    else:
        return send_from_directory('DOCROOT', site), 200

@app.errorhandler(404)
def not_found(e):
    return send_from_directory('templates', '404.html'), 404

@app.errorhandler(403)
def forbidden:
    return send_from_directory('templates', '403.html'), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
