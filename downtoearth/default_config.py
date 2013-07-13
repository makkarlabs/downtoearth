#Logging
LOG_FILE_LOC = 'flask_app/logs/error.log'

#Database
DB_USERNAME = ''
DB_PASSWORD = ''
DB_SERVER = ''
DB_NAME = ''

#Secret keys
SECRET_KEY = ''
SECRET_KEY_HASH = ''

#Mail settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
SENDER_EMAIL = ''

#Flask
DEBUG = True

#Celery
BROKER_URL = 'sqla+mysql://scott:tiger@localhost/scott'
CELERY_RESULT_BACKEND = "database"
CELERY_RESULT_DBURI = "mysql://scott:tiger@localhost/scott"

#FLASK-SECURITY CONFIG
SECURITY_REGISTERABLE = True
SECURITY_POST_LOGIN_VIEW = "/profile"

#FLASK SOCIAL CONFIG
CONSUMER_KEY = "645409828819862"
CONSUMER_SECRET = "fd51f4859ff0915e5d8e04638eb09227"
SOCIAL_APP_URL = "http://localhost:5000"
