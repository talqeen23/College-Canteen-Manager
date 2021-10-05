from pitho import app
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length
from flask import render_template,request,redirect,session
from pitho.models.user.model_changepassword import ChangePassword
class MyForm(FlaskForm):
	oldpassword=PasswordField("Old Password",validators=[DataRequired(),Length(min=8)])
	newpassword=PasswordField("New Password",validators=[DataRequired(),Length(min=8)])
	confirmpassword=PasswordField("Confirm Password",validators=[DataRequired(),Length(min=8)])
@app.route("/changepassword",methods=['GET','POST'])
def user_changepassword():
	if session.get("logged_in") is None :
		return redirect("/");
	message=""
	wform=MyForm(request.form)
	if wform.validate_on_submit():
		obj=ChangePassword()
		status=obj.resetpassword(request.form)
		if status==True:
			return redirect("/dashboard")
	return render_template("user/changepassword.html",data=message,form=wform)