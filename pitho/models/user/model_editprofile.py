from flask import Flask,flash,session
from pitho.Config import conn
class EditProfile():
	def update_profile(self,data):
		name=data.get("name")
		email=data.get("youremail")
		phone=data.get("phonenumber")
		user_id=session.get("logged_in")
		db=conn.connection.cursor()
		db.execute("select * from users where email=%s",(email))
		row=db.fetchone()
		if row is not None and row['id'] != user_id:
			flash("Email Already Exist")
			return False;
		db=conn.connection.cursor()
		db.execute("update users set email=%s, name=%s , phone=%s where id=%s",(email,name,str(phone),str(user_id)))
		conn.connection.commit()
		flash("Successful Update")
		return True;
	def getprofile_data(self):
		user_id=session.get("logged_in")
		db=conn.connection.cursor()
		db.execute("select * from users where id=%s",(str(user_id)))
		row=db.fetchone()
		return row