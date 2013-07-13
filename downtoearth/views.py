#Flask Imports
from flask import Flask, jsonify, flash, render_template, request, redirect, url_for, session, abort
from flask.ext.security import login_required, current_user, login_user

#App Imports
from flask_app import app, forms, db
from flask_app.models import User, Comment, Item, Vote
import config

#Python Imports
from datetime import datetime, date
import calendar
import json
import time

@app.route('/')
@login_required
def index():
    return render_template('index.html')

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
