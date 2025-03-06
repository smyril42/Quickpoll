from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin


__all__ = "db", "User"


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