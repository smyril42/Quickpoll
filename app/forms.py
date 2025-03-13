from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, FieldList, SelectField
from wtforms.fields.form import FormField
from wtforms.validators import DataRequired, Email, Optional


__all__ = "LoginForm", "SignupForm", "PollForm", "VoteForm"


class LoginForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class PollFieldForm(Form):
    name = StringField(validators=[])
    field_name = StringField('Name', validators=[DataRequired()])
    field_type = SelectField('Field Type', validators=[DataRequired()],
                             choices=[(100, "Single Choice"),
                                      (101, "Multi Choice"),
                                      (102, "Ranking"),
                                      (200, "Open Text")])
    answer_possibilities = FieldList(StringField('Answer'))


class PollForm(FlaskForm):
    name = StringField('Poll Name', validators=[DataRequired()])
    public_id = StringField('Public Identifier', validators=[DataRequired()])
    password = PasswordField('Password')
    open_date = DateField('Open on', validators=[Optional()])
    expiration_date = DateField('Close on', validators=[Optional()])
    type_ = SelectField("Type")
    fields = FieldList(FormField(PollFieldForm), min_entries=1)
    submit = SubmitField('Submit')


class VoteForm(FlaskForm):
    poll_id = StringField('Poll Identifier', validators=[DataRequired()])
    password = StringField('Poll Password')
    voting_code = StringField('Voting Code', validators=[DataRequired()])
    submit = SubmitField('Submit')
