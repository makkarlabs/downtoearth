from flask_app import db, app
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
     UserMixin, RoleMixin
from flask_app.forms import ExtendedRegisterForm
import json
import datetime

roles_users = db.Table('roles_users',
                db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

def date_serial(value):
    return value.strftime("%Y-%m-%d")+" "+value.strftime("%H:%M:%S")

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    organization = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
    backref=db.backref('users', lazy='dynamic'))

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(255), unique=True)
    store_url = db.Column(db.String(255))
    store_address = db.Column(db.String(1024))
    store_photo_url = db.Column(db.String(255))
    store_online = db_Column(db.Boolean())

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, )#TODO foreign key)
    item_name = db.Column(db.String(255))
    item_image_url = db.Column(db.String(255))
    item_price = db.Column(db.Numeric(20,3))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, )#TODO foreign key)
    comment = db.Column(db.String(2048))
    up_votes = db.Column(db.Integer)
    down_votes = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime())
    def __init__(self, item_id, comment):
        self.item_id = item_id
        self.comment = comment
        self.up_votes = 0
        self.down_votes = 0
        self.timestamp = datetime.now()

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    comment_id = db.Column(db.Integer)
    isup = db.Column(db.Boolean())
    timestamp = db.Column(db.DateTime())
    def __init__(self, user_id, comment_id, isup):
        self.user_id = user_id
        self.comment_id = comment_id
        self.isup = isup
        timestamp = datetime.now()

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, confirm_register_form=ExtendedRegisterForm)
