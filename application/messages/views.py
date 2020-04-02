from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from sqlalchemy.sql import text

from application import app, db
from application.messages.models import Message
from application.auth.models import User
from application.messages.forms import MessageForm
from application.messages.forms import UserFilterForm

@app.route("/messages", methods=["GET"])
def messages_index():
    return render_template("messages/list.html", message = Message.query.all())



#YET TO BE COMPLETED

@app.route("/messages/filter/user/")
def messages_filteruser_form():
    return render_template("messages/filteruserform.html", form = UserFilterForm())

@app.route("/messages/filter/user", methods=["GET", "POST"])
def messages_filteruser():
    form = UserFilterForm(request.form)

    if not form.validate():
        return render_template("messages/filteruserform.html", form = form)
    
    number = form.user.data

    order = text(SELECT )


    person = User.query.filter_by(id=number).first()
    
    message = Message.query.filter_by(account_id=person.id)

    return render_template("messages/filteruser.html", message)

####



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



@app.route('/messages/count')
def messages_count():
    return render_template("/messages/count.html", users=User.count_messages())



