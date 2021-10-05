from flask import Flask, flash, session
from pitho.Config import conn


class LoginModel():
	def logincheck(self, data):
		db = conn.connection.cursor()
		db.execute("select * from users where email=%s and password=%s", (data.get("youremail"), data.get("password")))
		row = db.fetchone()
		#db.commit();
		if row != None:
			#flash("successful login")
			session['logged_in'] = row['id']
			session['user_type'] = row['user_type']
			return True
		else:
			flash("invalid username and password")
			return False
