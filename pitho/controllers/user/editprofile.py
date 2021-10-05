from pitho import app
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Length
from flask import render_template,redirect,session,request
from pitho.models.user.model_editprofile import EditProfile
class MyForm(FlaskForm):
	name=StringField("Name",validators=[DataRequired()])
	youremail=StringField("Email",validators=[DataRequired()])
	phonenumber=StringField("Phone Number",validators=[DataRequired(),Length(min=10)])
@app.route("/editprofile",methods=['GET','POST'])
def user_editprofile():
	if session.get("logged_in") is None :
		return redirect("/");
	message=""
	obj=EditProfile()
	row=obj.getprofile_data()
	wform=MyForm(request.form,name=row['name'],youremail=row['email'],phonenumber=row['phone'])
	if wform.validate_on_submit():
		
		status=obj.update_profile(request.form)
		if status==True:
			return redirect("/dashboard")
	return render_template("user/editprofile.html",data=message,form=wform)
	