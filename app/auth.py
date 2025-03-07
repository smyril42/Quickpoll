import string

from flask import Blueprint, render_template, request, redirect, flash, url_for
from datetime import datetime
from hashlib import sha256
from random import SystemRandom
from flask_login import login_user, login_required, logout_user

from .database import db, User

blueprint = Blueprint('auth', __name__)

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    email = request.form.get('email')
    password = request.form.get('password')
    remember = bool(request.form.get('remember'))

    user = User.query.filter_by(email=email).first()
    if user is None or user.hashed_password != hashed(password, user.salt):
        flash('Invalid email or password! Please try again.')
        return redirect(url_for("auth.login"))
    login_user(user, remember=remember)
    return redirect(url_for("main.profile"))


@blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    if User.query.filter_by(email=email).first() is not None:
        flash("This email is already in use.")
        return redirect(url_for("auth.signup"))
    if User.query.filter_by(username=username).first() is not None:
        flash("This Username is already taken.")
        return redirect(url_for("auth.signup"))
    salt = generate_salt()
    db.session.add(
        User(username, email, hashed(password, salt), salt, datetime.today()))
    db.session.commit()
    return redirect(url_for("auth.login"))


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))


def generate_salt():
    return ''.join(SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(16))


def hashed(text, salt, iterations=3):
    assert iterations > 0
    for i in range(iterations):
        text = sha256((salt + text + salt).encode("utf-8")).hexdigest()
    return text
