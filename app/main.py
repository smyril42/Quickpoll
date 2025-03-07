from flask import Blueprint, render_template, request, send_file, redirect
from flask_login import login_required, current_user


blueprint = Blueprint("main", __name__)


@blueprint.route("/home")
@blueprint.route("/")
def home():
    return render_template("home.html", current_user=current_user)


@blueprint.route("/about")
def about():
    return render_template("about.html")


@blueprint.route("/help")
def help_page():
    return redirect("https://github.com/smyril42/Quickpoll/issues/new?labels=bug&template=bug-report.md")


@blueprint.route("/vote")
def vote():
    return render_template("vote.html")


@blueprint.route("/admin")
def admin():
    return render_template("admin.html")


@blueprint.route("/profile")
@login_required
def profile():
    return render_template("profile.html", username=current_user.username)


@blueprint.route("/static/<path:path>")
def static(filepath):
    if request.referrer != 'http://127.0.0.1/':
        return render_template('404.html')
    return send_file(filepath)
