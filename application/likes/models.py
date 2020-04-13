from application import db

class Like(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'),
                            nullable=False)

    def __init__(self, account_id, message_id):
        self.account_id = account_id
        self.message_id = message_id
