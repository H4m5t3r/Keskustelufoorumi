from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.messages.models import Message
from application.messages.forms import MessageForm

@app.route("/messages", methods=["GET"])
def messages_index():
    return render_template("messages/list.html", message = Message.query.all())

@app.route("/messages/new/")
@login_required
def messages_form():
    return render_template("messages/new.html", form = MessageForm())

@app.route("/messages/like/<message_id>/", methods=["POST"])
@login_required
def messages_set_liked(message_id):

    t = Message.query.get(message_id)
    t.liked = True
    db.session().commit()
  
    return redirect(url_for("messages_index"))

@app.route("/messages/unlike/<message_id>/", methods=["POST"])
@login_required
def messages_set_unlike(message_id):

    t = Message.query.get(message_id)
    t.liked = False
    db.session().commit()
  
    return redirect(url_for("messages_index"))

@app.route("/messages/", methods=["POST"])
@login_required
def messages_create():
    form = MessageForm(request.form)

    if not form.validate():
        return render_template("messages/new.html", form = form)

    t = Message(form.name.data, form.messagetext.data)
    t.account_id = current_user.id
  
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("messages_index"))


@app.route("/messages/delete/<message_id>/", methods=["POST"])
@login_required
def messages_delete(message_id):
    dele = Message.query.filter_by(id=message_id).first()
    db.session.delete(dele)
    db.session.commit()

    return redirect(url_for("messages_index"))
