from application import app, db
from flask import redirect, render_template, request, url_for
from application.messages.models import Message

@app.route("/messages", methods=["GET"])
def messages_index():
    return render_template("messages/list.html", message = Message.query.all())

@app.route("/messages/new/")
def messages_form():
    return render_template("messages/new.html")

@app.route("/messages/like/<message_id>/", methods=["POST"])
def messages_set_liked(message_id):

    t = Message.query.get(message_id)
    t.liked = True
    db.session().commit()
  
    return redirect(url_for("messages_index"))

@app.route("/messages/unlike/<message_id>/", methods=["POST"])
def messages_set_unlike(message_id):

    t = Message.query.get(message_id)
    t.liked = False
    db.session().commit()
  
    return redirect(url_for("messages_index"))

@app.route("/messages/", methods=["POST"])
def messages_create():
    t = Message(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("messages_index"))
