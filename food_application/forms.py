from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    # email, password, submit_button
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()
class RecipeForm(FlaskForm):
    
    id = StringField('id')
    title = StringField('Title')
    image = StringField('Image')
    summary = StringField('Summary')
    ingredients = StringField('Ingredients')
    instructions=StringField('Instructions')
    submit_button = SubmitField('Submit')
    date_created=StringField('Date_Created')
    cancel_button = SubmitField('Cancel')
