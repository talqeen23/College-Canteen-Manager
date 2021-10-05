from flask import Flask, flash, session
from pitho.Config import conn


class RegisterModel():
	def register(self, data):
		fname = str(data.get('fname'))
		lname = str(data.get('lname'))
		email = str(data.get('email'))
		password = str(data.get('password'))
		user_type = str(data.get('user_type'))
		name = fname+"    "+lname
		db = conn.connection.cursor()
		db.execute("select * from users where email=%s", email)
		row = db.fetchone()
		if row is None:
			db = conn.connection.cursor()
			#db.execute("insert into users(name,email,password,user_type) values ('"+name+"','"+email+"','"+password+"','"+user_type+"')")
			db.execute("insert into users(name,email,password,user_type) values(%s,%s,%s,%s)", (name, email, password, user_type))
			conn.connection.commit()
			flash("Successful Register")
			return True
		else:
			flash("Email is already exist")
			return False
