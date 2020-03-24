from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class MessageForm(FlaskForm):
    name = StringField("Message name", [validators.Length(min=2)])
    messagetext = StringField("Text")
 
    class Meta:
        csrf = False
