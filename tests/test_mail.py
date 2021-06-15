import unittest
from threading import Thread
from flask import Flask
from flask_mail import Mail, Message
from main import create_app

class TestMail(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(self)
        self.mail = Mail(self.app)
        self.app.push()
   
    def tearDown(self):
        self.app.pop()
        self.app_context.pop()
    
    def testApp(self):
        self.assertTrue(self.app.testing)
    
    def test_send(self):

        with self.mail.record_messages() as outbox:
            msg = Message(subject="testing",
                          recipients=["tester@example.com"],
                          body="test")
            self.mail.send(msg)
            self.assertIsNotNone(msg.date)
            self.assertEqual(len(outbox), 1)
            self.assertEqual(msg.sender, self.app.extensions['mail'].default_sender)

    def test_send_message(self):

        with self.mail.record_messages() as outbox:
            self.mail.send_message(subject="testing",
                                   recipients=["tester@example.com"],
                                   body="test")
            self.assertEqual(len(outbox), 1)
            msg = outbox[0]
            self.assertEqual(msg.subject, "testing")
            self.assertEqual(msg.recipients, ["tester@example.com"])
            self.assertEqual(msg.body, "test")
            self.assertEqual(msg.sender, self.app.extensions['mail'].default_sender)

