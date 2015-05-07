from flask.ext.sqlalchemy import SQLAlchemy 

db = SQLAlchemy() 

'''
Username Class 
'''

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userId = db.Column(db.Integer, db.ForeignKey('user.id'))
	firstName = db.Column(db.String(30))
	lastName = db.Column(db.String(30))
	userName = db.Column(db.String(30), unique=True)
	email = db.Column(db.String(30), unique=True)
	password = db.Column(db.String(30), unique = True)


	def __init__(self, firstName, lastName, username, email, 
		password, pointValue, totalPoints, quote, level, image, badge):
		self.firstName = firstname
		self.lastName = lastname
		self.username = username
		self.email = email
		self.password = password 
