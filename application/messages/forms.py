from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, TextAreaField, validators

class MessageForm(FlaskForm):
    name = StringField("Message name", [validators.Length(min=1, max=20)])
    messagetext = TextAreaField("Text", [validators.Length(min=1, max=2000)])

    class Meta:
        csrf = False

class UserFilterForm(FlaskForm):
    user = StringField("Name of the user", [validators.Length(min=1)])
 
    class Meta:
        csrf = False
