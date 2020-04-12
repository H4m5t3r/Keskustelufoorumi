from application import db
from application.models import Base
from application.categories.models import Category

class Message(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    messagetext = db.Column(db.String(144), nullable=False)
    liked = db.Column(db.Boolean, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)

    def __init__(self, name, messagetext):
        self.name = name
        self.messagetext = messagetext
        self.liked = False
        self.likes = 0
