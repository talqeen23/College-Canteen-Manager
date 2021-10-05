from pitho import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from flask import render_template, request, session, redirect
from pitho.models.user.model_register import RegisterModel


class MyForm(FlaskForm):
	fname = StringField("First Name", validators=[DataRequired()])
	lname = StringField("Last Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
	user_type = SelectField("User_Type", choices=[('1', "Student"), ('2', "Canteen Manager")])
	checkbox = BooleanField("Terms & Conditions")


@app.route("/register",methods=['GET', 'POST'])
def user_register():
	data = request.form
	wform = MyForm(request.form)
	obj = RegisterModel()
	if wform.validate_on_submit():
		status = obj.register(data)
		if status == True:
			return redirect("/")
	return render_template("user/register.html", form=wform)
