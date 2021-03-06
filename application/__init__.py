from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///messages.db"
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#functionality imports
from application import views

from application.messages import models
from application.messages import views

from application.auth import models
from application.auth import views

from application.categories import models
from application.categories import views

from application.answers import models
from application.answers import views

from application.likes import models
from application.likes import views

#Separate
from application.categories.models import Category

#login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
    # Adding the administrator account
    hashed_password = bcrypt.generate_password_hash("unlimitedpower").decode('utf-8')
    u = User("Administrator", "admin", hashed_password)
    db.session().add(u)
    db.session().commit()
    # Adding the first category
    c = Category("No category")
    c.account_id = 1
    db.session.add(c)
    db.session.commit()
except:
    pass
