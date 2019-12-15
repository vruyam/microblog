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
	LANGUAGES = ['en', 'es']

# (venv) $ export MAIL_SERVER=smtp.googlemail.com
# (venv) $ export MAIL_PORT=587
# (venv) $ export MAIL_USE_TLS=1
# (venv) $ export MAIL_USERNAME=<your-gmail-username>
# (venv) $ export MAIL_PASSWORD=<your-gmail-password>

# (venv) $ python -m smtpd -n -c DebuggingServer localhost:8025


# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-facelift

# moment('2017-09-28T21:45:23Z').format('L')
# "09/28/2017"
# moment('2017-09-28T21:45:23Z').format('LL')
# "September 28, 2017"
# moment('2017-09-28T21:45:23Z').format('LLL')
# "September 28, 2017 2:45 PM"
# moment('2017-09-28T21:45:23Z').format('LLLL')
# "Thursday, September 28, 2017 2:45 PM"
# moment('2017-09-28T21:45:23Z').format('dddd')
# "Thursday"
# moment('2017-09-28T21:45:23Z').fromNow()
# "7 hours ago"
# moment('2017-09-28T21:45:23Z').calendar()
# "Today at 2:45 PM"

# babel https://github.com/miguelgrinberg/microblog/tree/v0.13/app