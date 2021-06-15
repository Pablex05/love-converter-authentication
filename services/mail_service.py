from app import app
from flask_mail import Mail, Message
from flask import render_template
from threading import Thread


def sendMail(to, subject, template, **kwargs):
    msg = Message(subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template('mail/' + template + '.txt', **kwargs)
    msg.html = render_template('mail/' + template + '.html', **kwargs)
    thr = Thread(target=mail_sender, args=[app, msg])
    thr.start()  # Iniciar hilo


def mail_sender(app, msg):
    with app.app_context():
        Mail.send(msg)  # send es la que envia el mail
