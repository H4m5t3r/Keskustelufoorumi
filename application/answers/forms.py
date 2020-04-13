from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_login import current_user
from application.categories import models

class AnswerForm(FlaskForm):
    name = StringField("Title", [validators.Length(min=1, max=20)])
    
    answertext = TextAreaField("Text", [validators.Length(min=1, max=2000)])

    class Meta:
        csrf = False


class EditAnswerForm(FlaskForm):
    answertext = TextAreaField("Text", [validators.Length(min=1, max=2000)])

    class Meta:
        csrf = False


class UserFilterForm(FlaskForm):
    user = StringField("Name of the user", [validators.Length(min=1)])
 
    class Meta:
        csrf = False

