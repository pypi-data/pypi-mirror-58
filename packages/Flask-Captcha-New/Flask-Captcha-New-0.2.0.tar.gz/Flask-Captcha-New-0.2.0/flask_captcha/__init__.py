import logging
import re
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_captcha.models import db, CaptchaStore, CaptchaSequence

VERSION = (0, 2, 0)

class Captcha(object):
    ext_db = None

    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        logging.info('Initializing forked Flask-Captcha')
        with app.app_context():
            self.ext_db = current_app.extensions['sqlalchemy'].db
            active_metadata = self.ext_db.metadata
            CaptchaStore.__table__ = CaptchaStore.__table__.tometadata(active_metadata)
            CaptchaSequence.__table__ = CaptchaSequence.__table__.tometadata(active_metadata)

