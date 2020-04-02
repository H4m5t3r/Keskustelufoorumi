from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class MessageForm(FlaskForm):
    name = StringField("Message name", [validators.Length(min=1)])
    messagetext = StringField("Text", [validators.Length(min=1)])

    class Meta:
        csrf = False

class UserFilterForm(FlaskForm):
    user = StringField("Name of the user", [validators.Length(min=1)])
 
    class Meta:
        csrf = False
