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

@app.route("/likes/like/<message_id>", methods=["GET", "POST"])
@login_required
def likes_like(message_id):
    page = request.args.get("page", 1, type=int)
    answers = Answer.query.filter_by(message_id=message_id).order_by(Answer.id.desc()).paginate(page = page, per_page=5)
    
    message = Message.query.filter_by(id=message_id).first()
    l = Like.query.filter_by(message_id=message_id, account_id=current_user.id).first()
    if l:
        db.session.delete(l)
        db.session.commit()
        
        
        return render_template("messages/view_message.html", 
        message = message, 
        account = User.query.filter_by(id=message.account_id).first(), 
        category = Category.query.filter_by(id=message.category_id).first(), 
        answers = answers,
        answerwriters = User.query.all(), 
        likes = Like.query.filter_by(message_id=message_id).count())

    else:
        l = Like(current_user.id, message_id)
        db.session.add(l)
        db.session.commit()
        
        return render_template("messages/view_message.html", 
        message = message, 
        account = User.query.filter_by(id=message.account_id).first(), 
        category = Category.query.filter_by(id=message.category_id).first(), 
        answers = answers,
        answerwriters = User.query.all(), 
        likes = Like.query.filter_by(message_id=message_id).count())
