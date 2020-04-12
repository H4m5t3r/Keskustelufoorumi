from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, SignUpForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # possible validations
    user = User.query.filter_by(username=form.username.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user)
        return redirect(url_for("index"))
    
    else:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")


    


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/new/")
def auth_form():
    return render_template("auth/new.html", form = SignUpForm())

@app.route("/auth/", methods=["POST"])
def auth_create():
    form = SignUpForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    t = User(form.name.data, form.username.data, hashed_password)
  
    db.session().add(t)
    db.session().commit()

    flash('Your account was successfully created')
    return redirect(url_for("auth_login"))

