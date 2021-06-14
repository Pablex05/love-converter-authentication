from flask import redirect
from flask import request
from flask import url_for
from registration_form import *
from services.mail_functions import *

from app import *
from main.models import UserModel


@app.route('/register', methods=["POST"])
def register():
    user = UserModel(
        username=request.form['username'],
        password=request.form['password'],
        email=request.form['email']
    )

    assert (user.username is not None and user.password is not None and
            user.email is not None, 'Username, password or email are required'
            )

    # TODO agregar metodo para DB
    db = get_db()

    # TODO ver "validator/user" porque hace chequeo con email y no con username...
    if db.session.query(UserModel).filter(UserModel.username == user.username).scalar() is not None:
        return 'username already in use', 409

    else:
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))


@app.route('/login', methods=['POST'])
def login():
    db = get_db()
    user = db.session.query(UserModel).filter(UserModel.username ==
                                              request.get_json().get('username')).first_or_404()

    if user.validate_pass(request.get_json().get('password')):
        # Todavia no hay token.
        # access_token = create_access_token(identity=user)
        data = '{"id":"' + str(user.id) + '","username":"' + str(
            user.username) + '"}'  # + '","access_token":"' + access_token + '"}'

        return data, 200
    else:
        return 'Incorrect password', 401


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
