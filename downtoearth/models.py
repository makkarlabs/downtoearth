from downtoearth import db, app
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
     UserMixin, RoleMixin
import json
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
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
    active = db.Column(db.Boolean())
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

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(255), unique=True)
    store_url = db.Column(db.String(255))
    store_address = db.Column(db.String(1024))
    store_location = db.Column(db.String(255), default="All")
    store_photo_url = db.Column(db.String(255))
    store_online = db.Column(db.Boolean())

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer)
    item_name = db.Column(db.String(255))
    item_photo_url = db.Column(db.String(255))
    item_price = db.Column(db.Numeric(20,3))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(255))
    cat_id = db.Column(db.Integer)
    comment = db.Column(db.String(2048))
    up_votes = db.Column(db.Integer)
    down_votes = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime())
    def __init__(self,cat_name, comment, cat_id):
        self.cat_id = cat_id
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
security = Security(app, user_datastore)
social = Social(app, SQLAlchemyConnectionDatastore(db, Connection))


def list_restaurants_select():
    data=[]
    for store in Store.query.all():
        dat = store.id, store.store_name
        data.append(dat)
    return data
