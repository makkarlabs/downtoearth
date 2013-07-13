from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail, Message

import logging
import config

app = Flask(__name__)
app.config.from_object('flask_app.config')
filehandler = logging.FileHandler(filename=config.LOG_FILE_LOC)
filehandler.setLevel(logging.INFO)
app.logger.addHandler(filehandler)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + config.DB_USERNAME + ':' + config.DB_PASSWORD + '@' + config.DB_SERVER + '/' + config.DB_NAME

app.config['SOCIAL_FACEBOOK'] = {
    'consumer_key': config.CONSUMER_KEY,
    'consumer_secret': config.CONSUMER_SECRET
}

db = SQLAlchemy(app)
mail = Mail(app)

from flask_app import views
from flask_app import models, forms
#import hedge_app.tasks

#Uncomment on server
#if __name__ == '__main__':
#    app.run()
