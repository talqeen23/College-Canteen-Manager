from pitho import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email
from flask import render_template, request, redirect, session
from pitho.models.user.model_login import LoginModel


class MyForm(FlaskForm):
	youremail = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])


@app.route("/", methods=['GET', 'POST'])
def user_login():
	if session.get("logged_in") is not None :
		return redirect("/dashboard")
	message = ""
	data = request.form
	wform = MyForm(request.form)
	obj=LoginModel()
	if wform.validate_on_submit():
	#message=data.get("youremail")
		status = obj.logincheck(data)
		if status == True:
			if session.get('user_type') == 1:
				return redirect("/dashboard")
			elif session.get('user_type') == 2:
				return redirect("/author-dashboard")
	return render_template ("user/login.html", data=message, form=wform)


@app.route("/logout")
def logout():
	session['logged_in'] = None
	return redirect("/")
