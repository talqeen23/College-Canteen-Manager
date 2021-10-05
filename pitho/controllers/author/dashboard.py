from pitho import app
from flask import render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from pitho.models.author.model_dashboard import AuthorDashboard


class AuthorForm(FlaskForm):
	item_name = StringField("Item name:", validators=[DataRequired()])
	item_price = StringField("Item Price:", validators=[DataRequired()])
	submit = SubmitField("Add")


@app.route("/author-dashboard", methods=['GET', 'POST'])
def author_dashboard():
	aobj = AuthorDashboard()
	user_id = request.args.get('user')
	if user_id is None:
		user_id = 0
	users = aobj.get_user()
	form = AuthorForm(request.form)
	data = request.form
	if form.validate_on_submit():
		status = aobj.add_item(data)
		if status == True:
			return redirect("author-dashboard")
	item_list = aobj.item_list(user_id) 
	total = aobj.total_due_amount(user_id) 
	return render_template("author/dashboard.html", users_list=users, form=form, user_id=user_id, item_list=item_list, total=total)


@app.route("/author-dashboard/delete/<id>/<uid>", methods=['GET', 'POST'])
def delete_item(id, uid):
	aobj = AuthorDashboard()
	aobj.delete_item(id)
	return redirect("/author-dashboard?user="+str(uid))


@app.route("/author-dashboard/update", methods=['GET', 'POST'])
def update_item():
	uid = request.form.get('user_id')
	aobj = AuthorDashboard()
	aobj.update_item(request.form)
	return redirect("/author-dashboard?user="+str(uid))
