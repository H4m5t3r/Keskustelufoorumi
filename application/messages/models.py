from application import db
from application.models import Base

class Message(Base):

    messagetext = db.Column(db.String(144), nullable=False)
    liked = db.Column(db.Boolean, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, messagetext):
        self.name = name
        self.messagetext = messagetext
        self.liked = False
        self.likes = 0
