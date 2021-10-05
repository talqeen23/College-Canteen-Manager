import random
from flask import Flask,flash,session
from pitho.Config import conn
class ForgotPassword():
	def forgot_password(self,data):
		email=data.get("youremail")
		db=conn.connection.cursor()
		db.execute("select * from users where email=%s",(email))
		row=db.fetchone()
		if row is None:
			flash("Email Not Exist!")
			return False
		if session.get("otpshow") is None:
			db=conn.connection.cursor()	
			scode=random.randint(1000,9999)
			db.execute("update users set security_code=%s where email=%s",(str(scode),email))
			conn.connection.commit()
			session ['otpshow']=True
			return False
		if session.get("showpass") is None:
			db=conn.connection.cursor()
			otp=data.get("otp")
			db.execute("select * from users where email=%s and security_code=%s",(email,str(otp)))
			row=db.fetchone()
			if row is None:
				flash("Invalid Security Code")
				return False
			session['showpass']=True
			return False
		if session.get("otpshow") is not None and session.get("showpass") is not None:
			password=data.get("reset")
			db=conn.connection.cursor()	
			db.execute("update users set password=%s where email=%s",(str(password),email))
			conn.connection.commit()
			flash("Successfully Changed")
			return True
		return False
