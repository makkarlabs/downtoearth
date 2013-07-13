#Flask Imports
from flask import Flask, jsonify, flash, render_template, request, redirect, url_for, session, abort
from flask.ext.security import login_required, current_user, login_user, LoginForm

#App Imports
from downtoearth import app, forms, db
from downtoearth.models import User
import config

#Python Imports
from datetime import datetime, date
import calendar
import json
import time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template(
        'profile.html',
        content='Profile Page',
        facebook_conn=social.facebook.get_connection())

@app.route('/signin')
def login():
    if current_user.is_authenticated:
        return redirect('/profile')
    
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
