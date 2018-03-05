#!/usr/bin/env python
# encoding: utf-8
from main import app, db, loginManager

from models import User

from flask import render_template, request, session, abort, url_for, redirect

from flask_login import login_user, login_required, logout_user

import re


@loginManager.user_loader
def load_user(user_id):
    loaded_user = User.query.filter_by(id=user_id).first()
    if type(loaded_user) is str:
        return None
    else:
        return loaded_user


@app.route('/', methods=['GET', 'POST'])
def info():
    return render_template('info.html', session=session)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login-confirm', methods=['POST'])
def login_confirm():
    message = ""
    email = request.form['email']
    password = request.form['password']
    existing_user = User.query.filter_by(email=email).first()

    if not existing_user:
        message += "Nie ma takiego użytkownika w bazie. "
    else:
        if not existing_user.check_password(password):
            message += "Podano niepoprawne hasło. "
        else:
            # tutaj trzeba już dokonać operacji logowania
            db.session.commit()
            login_user(existing_user)
            return redirect(url_for('dashboard'))

    return render_template("login-failed.html", message=message)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return render_template('logout.html')


@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/register-confirm', methods=['POST'])
def register_confirm():

    is_okay_to_register = True
    is_email_okay = True
    message = ""

    username = request.form["username"]
    email = request.form["email"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    usertype = request.form["usertype"]
    about = request.form["about"]

    # Walidacja nazwy użytkownika ------------------------------------------
    if len(username) > 20:
        is_okay_to_register = False
        message += "Podana nazwa użytkownika jest zbyt długa. "
    # ----------------------------------------------------------------------

    # Walidacja adresu e-mail ----------------------------------------------
    if re.match("^[a-z0-9]+[\.'\-a-z0-9_]*[a-z0-9]+@+[a-z.0-9_]*[a-z.0-9_]\.[a-z]{2,4}$", email) is None:
        message += "Podano błędny adres e-mail. "
        is_okay_to_register = False
        is_email_okay = False
    elif len(email) > 30:
        message += "Podany adres e-mail jest zbyt długi. "
        is_okay_to_register = False
        is_email_okay = False
    # ----------------------------------------------------------------------

    # Walidacja hasła ------------------------------------------------------
    if password1 != password2:
        message += "Podane hasła różnią się. "
        is_okay_to_register = False
    elif len(password1) > 20 or len(password2) > 20:
        message += "Podane hasło jest zbyt długie. "
        is_okay_to_register = False
    # ----------------------------------------------------------------------

    # Sprawdzanie, czy przypadkiem nie istnieje już użytkownik o takim username i email w bazie
    if is_email_okay:
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            message += "Istnieje użytkownik o podanym adresie e-mail! Adres e-mail zajęty. "
            is_okay_to_register = False

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            message += "Istnieje użytkownik o podanej nazwie użytkownika! Nazwa użytkownika zajęta. "
            is_okay_to_register = False
    # -----------------------------------------------------------------------------------------

    # Walidacja tekstu 'o mnie' --------------------------------------------
    if len(about) > 200:
        is_okay_to_register = False
        message += "Napisałeś za dużo o sobie. Max 200 znaków. "
    # ----------------------------------------------------------------------

    # Po przejściu powyższych warunków można się zarejestrować: -------------------------------
    if is_okay_to_register:
        new_user = User()
        new_user.username = username
        new_user.email = email
        new_user.set_password(password1)
        new_user.usertype = usertype
        new_user.about = about
        db.session.add(new_user)
        db.session.commit()
        message = "Zarejestrowałeś się. Możesz się zalogować. "
    # -----------------------------------------------------------------------------------------

    return render_template("register-confirm.html", message=message)
