from flask import flash, url_for
from flask import redirect
from werkzeug.utils import secure_filename
import os.path
from registration_form import *
from services.mail_functions import *
from app import *
from main.models import UserModel
from flask_login import login_required, login_user, logout_user, current_user


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        user = UserModel(
            username=request.form['username'],
            password=request.form['password'],
            email=request.form['email']
        )
        db = get_db()

        assert (
            user.username is not None and
            user.password is not None and
            user.email is not None,
            'Username, password or email are required'
        )

        if db.session.query(UserModel).filter(UserModel.username == user.username).scalar() is not None:
            return 'username already in use', 409

        else:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))


"""

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
                       
"""
