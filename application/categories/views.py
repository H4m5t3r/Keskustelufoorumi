from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.categories.models import Category
from application.categories.forms import CategoryForm

@app.route("/categories/new/")
@login_required
def categories_form():
    return render_template("categories/new.html", form = CategoryForm(), categories = Category.query.all())

@app.route("/categories/", methods=["POST"])
@login_required
def categories_create():
    form = CategoryForm(request.form)

    if not form.validate():
        return render_template("categories/new.html", form = form)

    t = Category(form.name.data)
    t.account_id = current_user.id
  
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("categories_form"))
