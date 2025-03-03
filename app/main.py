from flask import Blueprint, render_template, request, send_file, redirect

blueprint = Blueprint("main", __name__)

@blueprint.route("/home")
@blueprint.route("/")
def home():
    return render_template("base.html")


@blueprint.route("/about")
def about():
    return redirect("https://github.com/smyril42/Quickpoll")

@blueprint.route("/help")
def help_page():
    return redirect("https://github.com/smyril42/Quickpoll/issues/new?labels=bug&template=bug-report.md")

@blueprint.route("/vote")
def vote():
    return render_template("vote.html")

@blueprint.route("/admin")
def admin():
    return render_template("admin.html")

@blueprint.route("/static/<path:path>")
def static(filepath):
    if request.referrer != 'http://127.0.0.1/':
        return render_template('404.html')
    return send_file(filepath)
