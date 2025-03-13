from string import ascii_letters, digits, punctuation
from datetime import datetime
from hashlib import sha256
from random import SystemRandom
from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user

from .database import db, User
from .forms import LoginForm, SignupForm


blueprint = Blueprint('auth', __name__)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or user.hashed_password != hashed(form.password.data, user.salt):
            flash('Invalid email or password! Please try again.')
            return redirect(url_for("auth.login"))
        login_user(user, remember=bool(form.remember.data))
        return redirect(url_for("main.profile"))
    elif form.errors:
        print(form.errors)
    return render_template('auth/login.html', form=form)


@blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data

        if User.query.filter_by(email=email).first() is not None:
            flash("This email is already in use.")
        elif User.query.filter_by(username=username).first() is not None:
            flash("This Username is already taken.")
        else:
            salt = generate_salt()
            db.session.add(
                User(username, email, hashed(form.password.data, salt), salt, datetime.today()))
            db.session.commit()
            return redirect(url_for("auth.login"))
    elif form.errors:
        print(form.errors)
    return render_template('auth/signup.html', form=form)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))


def generate_salt():
    return ''.join(SystemRandom().choice(ascii_letters + digits + punctuation) for _ in range(16))


def hashed(text, salt, iterations=3):
    assert iterations > 0
    for _ in range(iterations):
        text = sha256((salt + text + salt).encode("utf-8")).hexdigest()
    return text
