from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class CategoryForm(FlaskForm):
    name = StringField("The new category", [validators.Length(min=1, max=20)])
 
    class Meta:
        csrf = False
