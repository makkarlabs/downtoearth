#Flask Imports
from flask import Flask, jsonify, flash, render_template, request, redirect, url_for, session, abort
from flask.ext.security import login_required, current_user, login_user, LoginForm, RegisterForm
from flask.ext.social.views import connect_handler
from flask.ext.social.utils import get_provider_or_404

#App Imports
from downtoearth import app, forms, db
from downtoearth.models import User, social, security
from downtoearth.models import user_datastore as ds
import config
import facebook

#Python Imports
from datetime import datetime, date
import calendar
import json
import time

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template(
        'profile.html',
        content='Profile Page',
        facebook_conn=social.facebook.get_connection())

#You can write 'function decorators' like @login_required as shown below
#def subscription_required(fn):
#    @wraps(fn)
#    def decorated_view(*args, **kwargs):
#        print "subscribe"
#        if not is_subscribed(current_user):
#            return redirect('/subscribe')
#        return fn(*args, **kwargs)
#    return decorated_view

#def is_subscribed(user):
#    return User.query.filter_by(id=user.id).first().is_subscribed

@app.route('/adduser', methods=['GET', 'POST'])
@app.route('/adduser/<provider_id>', methods=['GET', 'POST'])
def adduser(provider_id=None):

    provider = get_provider_or_404(provider_id)

    form = RegisterForm()
    print form
    connection_values = session.get('failed_login_connection', None)
    print connection_values
    access_token = connection_values['access_token']
    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object("me")
    email = profile["email"]
    print email

    #ds = security.user_datastore
    user = ds.create_user(email=email, password="makkarlabsmass")
    ds.commit()
            # See if there was an attempted social login prior to registering
        # and if so use the provider connect_handler to save a connection
    connection_values = session.pop('failed_login_connection', None)

    if connection_values:
        connection_values['user_id'] = user.id
        connect_handler(connection_values, provider)

    if login_user(user):
        ds.commit()
        flash('Account created successfully', 'info')
        return redirect(url_for('profile'))


    return abort(404)

@app.route('/api/add_comment', methods=['POST'])
def add_comment():
    comment = Comment(request.form['item_id'], request.form['comment'])
    db.session.add(comment)
    db.session.commit()

@app.route('/api/up_vote', methods=['POST'])
def up_vote():
    try:
        vote = Vote(current_user.id, request.form['item_id'], request.form['comment_id'], True)
        db.session.add(vote)
        db.session.commit()
    except:
        print "Database error"
        return jsonify(data={"success":0, "error":"Database Error"})
    return jsonify(data={"success":1, "message":"Comment Up Voted"})

@app.route('/api/down_vote', methods=['POST'])
def down_vote():
    try:
        vote = Vote(current_user.id, request.form['item_id'], request.form['comment_id'], False)
        db.session.add(vote)
        db.session.commit()
    except:
        print "Database error"
        return jsonify(data={"success":0, "error":"Database Error"})
    return jsonify(data={"success":1, "message":"Comment Down Voted"})

@app.route('/api/can_vote', methods=['POST'])
def can_vote():
    comment = Comment.query.filter_by(user_id = current_user.id).filter_by(comment_id = request.form['comment_id']).all()
    if len(comment) > 0:
        return jsonify(data={"can_vote":False})
    else:
        return jsonify(data={"can_vote":True})    
