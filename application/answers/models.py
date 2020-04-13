from application import db
from application.models import Base
from application.categories.models import Category

class Answer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    answertext = db.Column(db.String(144), nullable=False)
    liked = db.Column(db.Boolean, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'),
                           nullable=False)

    def __init__(self, name, answertext):
        self.name = name
        self.answertext = answertext
        self.liked = False
        self.likes = 0

