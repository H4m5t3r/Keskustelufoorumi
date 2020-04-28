from application import db
from application.models import Base
from application.categories.models import Category

class Message(Base):
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    messagetext = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)

    def __init__(self, name, messagetext):
        self.name = name
        self.messagetext = messagetext
        self.likes = 0
