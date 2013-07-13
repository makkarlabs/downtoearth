from flask import Flask, session, url_for, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail, Message
from flask.ext.social import Social, SQLAlchemyConnectionDatastore, \
     login_failed
from flask.ext.social.utils import get_connection_values_from_oauth_response
import logging
import config

app = Flask(__name__)
app.config.from_object('downtoearth.config')
filehandler = logging.FileHandler(filename=config.LOG_FILE_LOC)
filehandler.setLevel(logging.INFO)
app.logger.addHandler(filehandler)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + config.DB_USERNAME + ':' + config.DB_PASSWORD + '@' + config.DB_SERVER + '/' + config.DB_NAME

app.config['SOCIAL_FACEBOOK'] = {
    'consumer_key': config.CONSUMER_KEY,
    'consumer_secret': config.CONSUMER_SECRET,
    'request_token_params': {'scope': 'email,publish_actions,user_photos'}
}

db = SQLAlchemy(app)
mail = Mail(app)

from downtoearth import views
from downtoearth import models, forms

class SocialLoginError(Exception):
    def __init__(self, provider):
        self.provider = provider

@login_failed.connect_via(app)
def on_login_failed(sender, provider, oauth_response):
    app.logger.debug('Social Login Failed via %s; '
                     '&oauth_response=%s' % (provider.name, oauth_response))
    session['failed_login_connection'] = \
        get_connection_values_from_oauth_response(provider, oauth_response)
    raise SocialLoginError(provider)


@app.errorhandler(SocialLoginError)
def social_login_error(error):
    return redirect(
        url_for('adduser', provider_id=error.provider.id, login_failed=1))
    

#import hedge_app.tasks

#Uncomment on server
#if __name__ == '__main__':
#    app.run()
