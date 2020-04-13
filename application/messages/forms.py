from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_login import current_user
from application.categories import models
from application.categories.models import Category

class MessageForm(FlaskForm):
    name = StringField("Title", [validators.Length(min=1, max=20)])
    
    messagetext = TextAreaField("Text", [validators.Length(min=1, max=2000)])
    
    category_id = QuerySelectField("Category", get_label="name",
        query_factory = lambda: models.Category.query.all())

    class Meta:
        csrf = False


class EditMessageForm(FlaskForm):
    messagetext = TextAreaField("Text", [validators.Length(min=1, max=2000)])
    
    category_id = QuerySelectField("Category", get_label="name",
        query_factory = lambda: models.Category.query.all())

    class Meta:
        csrf = False


class UserFilterForm(FlaskForm):
    user = StringField("Name of the user", [validators.Length(min=1)])
 
    class Meta:
        csrf = False
