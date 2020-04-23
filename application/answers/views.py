from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from sqlalchemy.sql import text

from application import app, db
from application.messages.models import Message
from application.auth.models import User
from application.answers.models import Answer
from application.answers.forms import AnswerForm, EditAnswerForm

@app.route("/answers/new/<message_id>", methods=["GET", "POST"])
@login_required
def answers_form(message_id):
    return render_template("answers/new.html", form = AnswerForm(), message_id = message_id)


@app.route("/answers/<message_id>", methods=["POST"])
@login_required
def answers_create(message_id):
    form = AnswerForm(request.form)

    if not form.validate():
        return render_template("messages/new.html", form = form)

    a = Answer(form.answertext.data)
    a.account_id = current_user.id
    a.message_id = message_id

    db.session().add(a)
    db.session().commit()
  
    return redirect(url_for("messages_index"))


@app.route("/answers/delete/<answer_id>/<message_id>/<writer_id>/<category_id>/", methods=["POST"])
@login_required
def answers_delete(answer_id, message_id, writer_id, category_id):
    dele = Answer.query.filter_by(id=answer_id).first()
    db.session.delete(dele)
    db.session.commit()

    return redirect(url_for("messages_view_message", message_id=message_id, writer_id=writer_id, category_id=category_id))