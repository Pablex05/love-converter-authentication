from werkzeug.security import check_password_hash, generate_password_hash

from main.extensions import db
from main.repositories import UserRepository

repository = UserRepository()


class User:
    """
        Acá va la lógica de negocio: llamar a un repo, hacer un cálculo, etc.
        Solamente ejecutan y devuelven algo.
    """

    # Password security management
    @property
    def plain_password(self):
        raise AttributeError("The password can not be obtained. It is prohibited.")
        # We won't obtain the password accessing with a get method

    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
        # We encrypt the plain text password from the JSON received in the user registration

    def validate_password(self, password):
        return check_password_hash(self.password, password)
        # Compares the received password with the database password

    @staticmethod
    def get_user_by_id(id):
        repository.get_register_by_id(id)

    @staticmethod
    def delete_user_by_id(id):
        repository.delete_register_by_id(id)

    @staticmethod
    def edit_user_by_id(id, data):
        repository.edit_register_by_id(id, data)

    @staticmethod
    def add_user(email, data):
        repository.create_register(email, data)
