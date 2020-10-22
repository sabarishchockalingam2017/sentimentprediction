from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class InputForm(FlaskForm):
    userinput = StringField('UserInput')
    submit = SubmitField('Enter')