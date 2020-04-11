from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, ValidationError
from application.categories.models import Category

class CategoryForm(FlaskForm):
    name = StringField("The new category", [validators.Length(min=1, max=20)])
 
    def validate_name(self, name):
        category = Category.query.filter_by(name=name.data).first()

        if category:
            raise ValidationError('That category already exists.')

    class Meta:
        csrf = False
