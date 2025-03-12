from flask import Blueprint, render_template, request, send_file, redirect
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound


from app.forms import PollForm


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
    return redirect(
        "https://github.com/smyril42/Quickpoll/issues/new?labels=bug&template=bug-report.md"
    )


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
        raise NotFound()
    return send_file(filepath)


@blueprint.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = PollForm()
    if form.validate_on_submit():
        poll_name = form.name.data
        public_identifier = form.public_id.data
        password = form.password.data
        open_date = form.open_date.data
        expiration_date = form.expiration_date.data
        fields = form.fields.data

        print(poll_name, public_identifier, password, open_date, expiration_date, fields)
    else:
        print(form.errors)

    return render_template('create_election.html', form=form)
