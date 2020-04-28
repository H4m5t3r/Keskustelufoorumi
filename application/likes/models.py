from application import db
from application.models import Base

class Like(Base):

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'),
                            nullable=False)

    def __init__(self, account_id, message_id):
        self.account_id = account_id
        self.message_id = message_id
