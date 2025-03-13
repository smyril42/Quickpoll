from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin


__all__ = "db", "User", "Poll", "Question"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(db.String, nullable=False)
    salt: Mapped[str] = mapped_column(db.String, nullable=False)
    creation_date = mapped_column(db.DateTime, nullable=False)
    is_admin: Mapped[int] = mapped_column(db.Boolean, nullable=False, default=0)

    def __init__(self, username, email, hashed_password, salt, creation_date, is_admin=None):
        self.username = username
        self.email = email
        self.hashed_password=hashed_password
        self.salt=salt
        self.creation_date=creation_date
        self.is_admin=0 if is_admin is None else is_admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Poll(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    owner_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    public_id: Mapped[int] = mapped_column(db.Integer, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(db.String)
    salt: Mapped[str] = mapped_column(db.String)
    creation_date = mapped_column(db.DateTime)
    open_date = mapped_column(db.DateTime)
    expiration_date = mapped_column(db.DateTime)

    questions = db.relationship("Question")

    def __init__(self, owner_id, name, public_id, hashed_password, salt, open_date, expiration_date):
        self.owner_id = owner_id
        self.name = name
        self.public_id = public_id
        self.hashed_password=hashed_password
        self.salt=salt
        self.creation_date=datetime.today()
        self.open_date=open_date
        self.expiration_date=expiration_date


class Question(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    poll_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("poll.id"), nullable=False)
    type_: Mapped[int] = mapped_column(db.Integer, nullable=False)
    choice0: Mapped[str] = mapped_column(db.String)
    choice1: Mapped[str] = mapped_column(db.String)
    choice2: Mapped[str] = mapped_column(db.String)
    choice3: Mapped[str] = mapped_column(db.String)
    choice4: Mapped[str] = mapped_column(db.String)

    def __init__(self, name, poll_id, type_, choices: list):
        self.name = name
        self.poll_id=poll_id
        self.type_=type_
        self.choice0, self.choice1, self.choice2, self.choice3, self.choice4=choices
