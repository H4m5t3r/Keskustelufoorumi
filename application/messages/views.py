from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from sqlalchemy.sql import text

from application import app, db
from application.messages.models import Message
from application.auth.models import User
from application.categories.models import Category
from application.answers.models import Answer
from application.likes.models import Like
from application.messages.forms import MessageForm, EditMessageForm

@app.route("/messages", methods=["GET"])
def messages_index():
    return render_template("messages/list.html", message = Message.query.order_by(Message.id.desc()), account = User.query.all())

@app.route("/messages/view/<message_id>/<writer_id>/<category_id>", methods=["GET"])
def messages_view_message(message_id, writer_id, category_id):
    return render_template("messages/view_message.html", 
    message = Message.query.filter_by(id=message_id).first(), 
    account = User.query.filter_by(id=writer_id).first(), 
    category = Category.query.filter_by(id=category_id).first(), 
    answers = Answer.query.filter_by(message_id=message_id),
    answerwriters = User.query.all(), 
    likes = Like.query.filter_by(message_id=message_id).count())


@app.route("/messages/new/")
@login_required
def messages_form():
    return render_template("messages/new.html", form = MessageForm())


@app.route("/messages/editform/<message_id>", methods=["GET", "POST"])
@login_required
def messages_edit_form(message_id):
    m = Message.query.filter_by(id=message_id).first()
    preset = EditMessageForm()
    preset.messagetext.data = m.messagetext
    preset.category_id.data = m.category_id
    return render_template("messages/edit.html", form = preset, message_id = m.id)


@app.route("/messages/", methods=["POST"])
@login_required
def messages_create():
    form = MessageForm(request.form)

    if not form.validate():
        return render_template("messages/new.html", form = form)

    t = Message(form.name.data, form.messagetext.data)
    t.account_id = current_user.id
    t.category_id = request.form['category_id']

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("messages_index"))



@app.route("/messages/edit/<message_id>/", methods=["POST"])
@login_required
def messages_edit(message_id):
    form = EditMessageForm(request.form)
    if not form.validate():
        m = Message.query.filter_by(id=message_id).first()
        return render_template("messages/edit.html", form = form, message_id = m.id)
    
    edit = Message.query.filter_by(id=message_id).first()
    if edit.messagetext == request.form['messagetext'] and edit.category_id == request.form['category_id']:
        return redirect(url_for("messages_index"))
    else:
        edit.messagetext = form.messagetext.data
        edit.category_id = request.form['category_id']
        db.session().commit()
        return redirect(url_for("messages_index"))


@app.route("/messages/delete/<message_id>/", methods=["POST"])
@login_required
def messages_delete(message_id):
    answersToDelete = Answer.query.filter_by(message_id=message_id)
    db.session.delete(Message.query.filter_by(id=message_id).first())
    answersToDelete.delete()
    db.session.commit()

    return redirect(url_for("messages_index"))


@app.route('/messages/count')
def messages_count():
    return render_template("/messages/count.html", users=User.count_messages())



