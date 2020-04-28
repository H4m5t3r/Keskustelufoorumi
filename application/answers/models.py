from application import db
from application.models import Base
from application.categories.models import Category

class Answer(Base):

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    answertext = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'),
                           nullable=False)

    def __init__(self, answertext):
        self.answertext = answertext
        self.liked = False
        self.likes = 0
