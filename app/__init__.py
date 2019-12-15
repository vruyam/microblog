from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel
from flask_babel import lazy_gettext as _l

import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()

login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	db.init_app(app)
	migrate.init_app(app, db)
	login.init_app(app)
	mail.init_app(app)
	bootstrap.init_app(app)
	moment.init_app(app)
	babel.init_app(app)

	from app.errors import bp as errors_bp
	app.register_blueprint(errors_bp)
	from app.auth import bp as auth_bp
	app.register_blueprint(auth_bp, url_prefix='/auth')
	from app.blog import bp as blog_bp
	app.register_blueprint(blog_bp, url_prefix='/blog')

	from app import models

	@app.shell_context_processor
	def make_shell_context():
	    return {'db': db, 'User': models.User, 'Post': models.Post}

	if not app.debug:
		if app.config['MAIL_SERVER']:
			auth = None
			if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
				auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
			secure = None
			if app.config['MAIL_USE_TLS']:
				secure = ()
			mail_handler = SMTPHandler(
				mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
				fromaddr=app.config['MAIL_USERNAME'],
				toaddrs=app.config['ADMINS'], subject='Microblog Failure',
				credentials=auth, secure=secure)
			mail_handler.setLevel(logging.ERROR)
			app.logger.addHandler(mail_handler)
		if not os.path.exists('logs'):
			os.mkdir('logs')
		file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,backupCount=10)
		file_handler.setFormatter(logging.Formatter(
			'%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
		file_handler.setLevel(logging.INFO)
		app.logger.addHandler(file_handler)

		app.logger.setLevel(logging.INFO)
		app.logger.info('Microblog startup')
	return app