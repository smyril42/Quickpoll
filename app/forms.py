from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, FieldList, SelectField
from wtforms.fields.form import FormField
from wtforms.validators import DataRequired, Email, Optional, Length


__all__ = "LoginForm", "SignupForm", "PollForm", "VoteForm"


class LoginForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Register')


class PollFieldForm(Form):
    name = StringField(validators=[])
    field_name = StringField('Name', validators=[DataRequired()])
    field_type = SelectField('Field Type', validators=[DataRequired()],
                             choices=[(100, "Single Choice"),
                                      (101, "Multi Choice"),
                                      (102, "Ranking"),
                                      (200, "Open Text")])
    choices = FieldList(StringField('Answer'))


class PollForm(FlaskForm):
    name = StringField('Poll Name', validators=[DataRequired()])
    public_id = StringField('Public Identifier', validators=[DataRequired()])
    password = PasswordField('Password')
    open_date = DateField('Open on', validators=[Optional()])
    expiration_date = DateField('Close on', validators=[Optional()])
    fields = FieldList(FormField(PollFieldForm), min_entries=1)
    submit = SubmitField('Submit')


class VoteFieldForm(FlaskForm):
    field_name = StringField('Vote Name', validators=[DataRequired()])
    type_ = SelectField('Vote Type', validators=[DataRequired()])
    choices = FieldList(FormField(StringField))


class VoteForm(FlaskForm):
    poll_id = StringField('Poll Identifier', validators=[DataRequired()])
    voting_code = PasswordField('Voting Code', validators=[DataRequired()])

    includes_content = BooleanField('Includes Content', default=True)

    fields = FieldList(FormField(VoteFieldForm), validators=[Optional()])

    submit = SubmitField('Enter')
