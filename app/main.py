from flask import Blueprint, render_template, request, send_file, redirect, flash
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from .forms import PollForm, VoteForm
from .database import db, Poll, Question
from .auth import hashed, generate_salt

bp = Blueprint("main", __name__)


@bp.route("/home")
@bp.route("/")
def home():
    return render_template("home.html", current_user=current_user)


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/help")
def help_page():
    return redirect(
        "https://github.com/smyril42/Quickpoll/issues/new?labels=bug&template=bug-report.md"
    )


@bp.route("/vote", methods=["GET", "POST"])
def vote():
    hidden = True
    form = VoteForm()
    if form.validate_on_submit():
        poll = Poll.query.filter_by(public_id=form.poll_id.data).first()
        if poll is None:
            flash("Poll not found!")
            return render_template("vote.html", form=form, hidden=hidden)

        hashed_secret = hashed(form.voting_code.data, poll.salt)

        # if password/code is incorrect
        if not (
                poll.hashed_password and hashed_secret == poll.hashed_password or
                (not poll.hashed_password and hashed_secret in [i["hashed_code"] for i in poll.codes])
        ):
            flash("Invalid Code/Password!")
            return render_template("vote.html", form=form, hidden=hidden)

        hidden = False
        for question in poll.questions:
            form.fields.append_entry()
            form.fields[-1].type_ = question.type_
            form.fields[-1].field_name = question.name
            form.fields[-1].choices = question.choices if (question.type_ // 100) == 1 else tuple()

        if form.includes_content.data:
            ...

    elif form.errors:
        print(form.errors)

    return render_template("vote.html", form=form, hidden=hidden)


@bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html", username=current_user.username)


@bp.route("/static/<path:path>")
def static(filepath):
    if request.referrer != 'http://127.0.0.1/':
        raise NotFound()
    return send_file(filepath)


@bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = PollForm()
    if request.method=="POST": #form.validate_on_submit():
        public_identifier = form.public_id.data
        if Poll.query.get(public_identifier):
            flash("This Identifier is already in use!")
        else:
            pw = form.password.data
            salt = generate_salt() if pw else None
            hashed_pw = hashed(pw, salt) if pw else None
            poll = Poll(current_user.id, form.name.data, public_identifier, hashed_pw,
                        salt, form.open_date.data, form.expiration_date.data)
            db.session.add(poll)
            db.session.flush()
            db.session.add_all([Question(
                field["field_name"], poll.id, field["field_type"], field["choices"]
            ) for field in form.fields.data])
            db.session.commit()
    elif form.errors:
        print(form.errors)

    return render_template('create_poll.html', form=form)
