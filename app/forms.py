from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField, FieldList, SelectField
from wtforms.fields.form import FormField
from wtforms.validators import DataRequired, Email


__all__ = "LoginForm", "SignupForm"


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


class PollFieldForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    field_name = StringField('Name', validators=[DataRequired()])
    field_type = SelectField('Field Type', validators=[DataRequired()],
                             choices=[(0, "Single Choice"),
                                      (1, "Multi Choice"),
                                      (2, "Open Text")])
    #answer_possibilities = FieldList(StringField('Answer', validators=[DataRequired()]))


class PollForm(FlaskForm):
    name = StringField('Poll Name', validators=[DataRequired()])
    public_id = StringField('Public Identifier', validators=[DataRequired()])
    password = PasswordField('Password')
    open_date = DateField('Open on')
    expiration_date = DateField('Close on')
    fields = FieldList(FormField(PollFieldForm), min_entries=1)
    submit = SubmitField('Submit')
