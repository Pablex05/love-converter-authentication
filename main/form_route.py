from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, TextField
from wtforms import validators
from wtforms.fields.html5 import EmailField


class UserRegistration(FlaskForm):

    # Username validation function
    def validator_field(form, field):
        # Verify that it does not contain underscores or hashtag
        if (field.data.find("_") != -1) or (field.data.find("#") != -1):
            # Show validation error
            raise validators.ValidationError("The field can only contain letters and numbers")

    def optional(field):
        field.validators.insert(0, validators.Optional())

    user = TextField('Username',
                     [
                         validators.Required(message="fill the field with an username"),
                         validators.length(min=4, max=25, message='The length of the username is not valid'),
                         validator_field
                     ])

    # No definido en el model de usuarios
    """   name = TextField('Name',
                        [
                            validators.Required(message="fill the field with a name"),
                            validators.length(min=4, max=25, message='The length of the name is not valid'),
                            validator_field
                        ])
   
       lastname = TextField('Lastname',
                            [
                                validators.Required(message="fill the field with a lastname"),
                                validators.length(min=4, max=25, message='The length of the lastname is not valid'),
                                validator_field
                            ])"""

    password = PasswordField('Password',
                             [
                                 validators.Required(),
                                 validators.length(min=12, message="The password must be more than 12 characters"),
                                 validators.EqualTo("confirm", message="Password does not match")
                             ])

    confirm = PasswordField("Repeat password")

    email = EmailField('Email',
                       [
                           validators.Required(message="fill the field with an email"),
                           validators.Email(message='Wrong email format')
                       ])

    # Definition of submit field
    submit = SubmitField("Send")


# Ya definida en "validator\user.py"
"""# Check if the email already exists in the Data Base
def validate_email(self, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Email already exists')"""

# No se usa mas
"""def existence_validator(email):
    aux = False

    if db.session.query(User).filter(User.email.ilike(email)).count() == 0:
        aux = True
    return aux"""
