import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 8025)
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	ADMINS = ['mayur.verlekar@parinati.in',]
	POSTS_PER_PAGE = 3

# (venv) $ export MAIL_SERVER=smtp.googlemail.com
# (venv) $ export MAIL_PORT=587
# (venv) $ export MAIL_USE_TLS=1
# (venv) $ export MAIL_USERNAME=<your-gmail-username>
# (venv) $ export MAIL_PASSWORD=<your-gmail-password>

# (venv) $ python -m smtpd -n -c DebuggingServer localhost:8025