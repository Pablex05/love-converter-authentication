import unittest
from werkzeug.security import generate_password_hash, check_password_hash

from main import create_app
from main.services.user import UserService


class TestAuth(unittest.TestCase):

    def set_up(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tear_down(self):
        self.app_context.pop()

    def test_pass_encrypt(self):
        password = "123456"
        pwhash = generate_password_hash(password)
        self.assertTrue(check_password_hash(pwhash, password))

    def test_user_service_check_password(self):
        # Llamamos al servicio de user
        service = UserService()
        self.assertTrue(service.check_pwd("password"))
