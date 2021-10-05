from pitho import app
from flask import render_template, request, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from pitho.models.author.model_item_list import ItemList


class ListForm(FlaskForm):
	item_name = StringField("Item Name:", validators=[DataRequired()])
	item_price = StringField("Item Price:", validators=[DataRequired()])
	submit = SubmitField("Add")


@app.route("/item-list", methods=['GET', 'POST'])
def item_list():
	aobj = ItemList()
	form = ListForm(request.form)
	data = request.form
	if form.validate_on_submit():
		status = aobj.add_list(data)
		if status == True:
			return redirect("item-list")
	item_list = aobj.item_list()
	author_id = session.get('logged_in')
	return render_template("author/item_list.html", form=form, item_list=item_list, author_id=author_id)


@app.route("/item-list/delete/<id>/<uid>", methods=['GET', 'POST'])
def delete(id, uid):
	aobj = ItemList()
	aobj.delete(id)
	
	return redirect("/item-list")


@app.route('/get-item-list/<id>')
def get_item_list(id):
	aobj = ItemList()
	data = aobj.item(id)
	return data
