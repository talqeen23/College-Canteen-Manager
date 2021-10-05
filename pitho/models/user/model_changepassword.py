from flask import Flask,flash,session
from pitho.Config import conn
class ChangePassword():
	def resetpassword(self,data):
		oldpass=data.get("oldpassword")
		newpass=data.get("newpassword")
		confirmpass=data.get("confirmpassword")
		if newpass==confirmpass:
			user_id=session.get("logged_in")
			db=conn.connection.cursor()
			db.execute("select * from users where id=%s and password=%s",(str(user_id),oldpass))
			row=db.fetchone()
			if row is None:
				flash("please check your old password")
				return False;
			db=conn.connection.cursor()
			db.execute("update users set password=%s where id=%s ",(newpass,str(user_id)) )
			conn.connection.commit()
			flash("successful change your password")
			return True;
		flash("password did not match")
		return False;
		