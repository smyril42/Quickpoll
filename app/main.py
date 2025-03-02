from flask import Blueprint, render_template, request, send_from_directory, send_file

blueprint = Blueprint("main", __name__)

@blueprint.route("/home")
@blueprint.route("/")
def home():
    return render_template("base.html")


@blueprint.route("/static/<path:path>")
def static(filepath):
    if request.referrer != 'http://127.0.0.1/':
        return render_template('404.html')
    return send_file(filepath)
