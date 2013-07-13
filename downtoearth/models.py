from downtoearth import db, app
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
     UserMixin, RoleMixin
from downtoearth.forms import ExtendedRegisterForm
import json
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore


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
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
    backref=db.backref('users', lazy='dynamic'))
    connections = db.relationship('Connection',
                backref=db.backref('user', lazy='joined'), cascade="all")

class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)

class store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(255), unique=True)
    store_url = db.Column(db.String(255))
    store_address = db.Column(db.String(1024))
    store_photo_url = db.Column(db.String(255))
    store_online = db.Column(db.Boolean())

class item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, )#TODO foreign key)
    item_name = db.Column(db.String(255))
    item_image_url = db.Column(db.String(255))
    item_price = db.Column(db.Numeric(20,3))

class comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, )#TODO foreign key)
    comment = db.Column(db.String(2048))
    up_votes = db.Column(db.Integer)
    down_votes = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime())

class votes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    item_id = db.Column(db.Integer)
    comment_id = db.Column(db.Integer)
    isup = db.Column(db.Boolean())
    timestamp = db.Column(db.DateTime())

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
print "social created"
social = Social(app, SQLAlchemyConnectionDatastore(db, Connection))

