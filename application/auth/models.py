from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False, unique=True)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)

    messages = db.relationship("Message", backref='account', lazy=True)

    def __init__(self, name):
        self.name = name

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


    @staticmethod
    def count_messages():
        stmt = text("SELECT Account.name, COUNT(Message.id) FROM Account "
        "LEFT JOIN Message ON Message.account_id = Account.id "
        "GROUP BY Account.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "messages":row[1]})

        return response

    @staticmethod
    def people_who_have_liked(message_id):
        stmt = text("SELECT Account.name FROM Account WHERE Account.id "
        "IN (SELECT Like.account_id FROM Like WHERE Like.message_id = :message_id) ORDER BY Account.name").params(message_id=message_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})

        return response
