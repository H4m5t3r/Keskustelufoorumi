from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from sqlalchemy.sql import text

from application import app, db
from application.messages.models import Message
from application.auth.models import User
from application.likes.models import Like
from application.answers.models import Answer
from application.categories.models import Category
from application.messages.forms import MessageForm, EditMessageForm
from application.messages.forms import UserFilterForm

@app.route("/likes/like/<message_id>", methods=["GET", "POST"])
def likes_like(message_id):
    message = Message.query.filter_by(id=message_id).first()
    l = Like.query.filter_by(message_id=message_id, account_id=current_user.id).first()
    if l:
        db.session.delete(l)
        message.likes = message.likes - 1
        db.session.commit()
        return render_template("messages/view_message.html", 
        message = message, 
        account = User.query.filter_by(id=message.account_id).first(), 
        category = Category.query.filter_by(id=message.category_id).first(), 
        answers = Answer.query.filter_by(message_id=message_id),
        answerwriters = User.query.all())

    else:
        l = Like(current_user.id, message_id)
        db.session.add(l)
        message.likes = message.likes + 1
        db.session.commit()
        return render_template("messages/view_message.html", 
        message = message, 
        account = User.query.filter_by(id=message.account_id).first(), 
        category = Category.query.filter_by(id=message.category_id).first(), 
        answers = Answer.query.filter_by(message_id=message_id),
        answerwriters = User.query.all())