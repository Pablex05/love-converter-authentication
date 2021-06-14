from flask import flash
from flask import redirect
from werkzeug.utils import secure_filename
import os.path
from registration_form import *
from services.mail_functions import *
from app import *
from flask_login import login_required, login_user, logout_user, current_user


@app.route('/user_registration', methods=["POST", "GET"])
def user_registration():
    title = "User Registration"
    login_form = LoginForm()
    form = UserRegistration()

    if form.validate_on_submit():
        if existence_validator(form.email.data):
            user = User(name=form.name.data, lastname=form.lastname.data,
                        user=form.user.data, email=form.email.data,
                        password=form.password.data)
            db.session.add(user)
            db.session.commit()

            flash('User created successfully', 'success')
            sendMail(form.email.data, 'Welcome to Love Convert', 'user_created', form=form)

            login_user(user, True)
            return redirect(url_for('index'))
        else:
            flash('There is an account registered with the email. Try to recover your password', 'danger')

    return render_template('user_form.html', title=title, form=form,
                           login_form=login_form, destination=user_registration)