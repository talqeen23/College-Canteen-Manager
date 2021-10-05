from pitho import app
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length,Email
from flask import render_template,request,redirect,session
from pitho.models.user.model_reset import ForgotPassword

class MyForm(FlaskForm):
	youremail=StringField("Email",validators=[DataRequired(),Email()])
	otp=StringField("OTP")
	reset=PasswordField("Enter Your New Password")

@app.route("/reset",methods=['GET','POST'])
def user_reset():
	if session.get("logged_in") is not None:
		return redirect ("/")
	
	message=""
	otp_status=False
	pass_status=False
	
	data=request.form;
	wform=MyForm(request.form)
	if wform.validate_on_submit():
		obj=ForgotPassword()
		status=obj.forgot_password(request.form)
		if status==True:
			return redirect("/")
	if session.get('otpshow') is not None:
		otp_status=True
	if session.get('showpass') is not None:
		pass_status=True
	return render_template("user/reset.html",data=message,form=wform,otp=otp_status,passw=pass_status)
	
