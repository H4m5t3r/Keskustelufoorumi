from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from sqlalchemy.sql import text

from application import app, db
from application.messages.models import Message
from application.auth.models import User
from application.answers.models import Answer
from application.answers.forms import AnswerForm, EditAnswerForm

@app.route("/answers/new/<message_id>/<writer_id>/<category_id>", methods=["GET", "POST"])
@login_required
def answers_form(message_id, writer_id, category_id):
    return render_template("answers/new.html", form = AnswerForm(), message_id = message_id, writer_id = writer_id, category_id = category_id)

@app.route("/answers/edit/<answer_id>/<message_id>/<writer_id>/<category_id>", methods=["GET", "POST"])
@login_required
def answers_edit_form(answer_id, message_id, writer_id, category_id):
    a = Answer.query.filter_by(id=answer_id).first()
    preset = AnswerForm()
    preset.answertext.data = a.answertext
    
    return render_template("answers/edit.html", form = preset, answer_id = answer_id, message_id = message_id, writer_id = writer_id, category_id = category_id)


@app.route("/answers/<message_id>/<writer_id>/<category_id>", methods=["POST"])
@login_required
def answers_create(message_id, writer_id, category_id):
    form = AnswerForm(request.form)

    if not form.validate():
        return render_template("answers/new.html", form = form, message_id = message_id, writer_id = writer_id, category_id = category_id)

    a = Answer(form.answertext.data)
    a.account_id = current_user.id
    a.message_id = message_id

    db.session().add(a)
    db.session().commit()
  
    return redirect(url_for("messages_view_message", message_id=message_id, writer_id = writer_id, category_id = category_id))


@app.route("/answers/delete/<answer_id>/<message_id>/<writer_id>/<category_id>/", methods=["POST"])
@login_required
def answers_delete(answer_id, message_id, writer_id, category_id):
    dele = Answer.query.filter_by(id=answer_id).first()
    if not dele.account_id == current_user.id and not current_user.id == 1:
        return redirect(url_for("messages_view_message", message_id=message_id, writer_id=writer_id, category_id=category_id))
    
    db.session.delete(dele)
    db.session.commit()

    return redirect(url_for("messages_view_message", message_id=message_id, writer_id=writer_id, category_id=category_id))

@app.route("/answers/editconfirm/<answer_id>/<message_id>/<writer_id>/<category_id>", methods=["POST"])
@login_required
def answers_edit(answer_id, message_id, writer_id, category_id):
    form = AnswerForm(request.form)
    if not form.validate():
        return render_template("answers/edit.html", form = form, answer_id = answer_id, message_id=message_id, writer_id=writer_id, category_id=category_id)
    
    answer = Answer.query.filter_by(id=answer_id).first()
    if not answer.account_id == current_user.id:
        return redirect(url_for("messages_view_message", message_id=message_id, writer_id=writer_id, category_id=category_id))
    
    answer.answertext = form.answertext.data
    db.session.commit()
    return redirect(url_for("messages_view_message", message_id=message_id, writer_id=writer_id, category_id=category_id))
