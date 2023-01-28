from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class signupform(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()

class loginForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField()

class AddtocartForm(FlaskForm):
    title = StringField("Title", validators = [DataRequired()])
    img_url = StringField("Image URL", validators = [DataRequired()])
    caption = StringField("Caption", validators = [])
    
    submit = SubmitField()

class SearchForm(FlaskForm):
    search = StringField('What are you looking for', validators=[DataRequired()])

    find = SubmitField()
