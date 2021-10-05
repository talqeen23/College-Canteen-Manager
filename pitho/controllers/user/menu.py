from pitho import app
from pitho.models.user.model_menu import UserMenu
from flask import render_template, request, session, redirect


@app.route("/menu", methods=['GET', 'POST'])
def user_menu():
	aobj = UserMenu()
	if session.get("logged_in") is None:
		return redirect("/")
	if session.get("user_type") == 2:
		return redirect("/author-dashboard")
	id = session.get("logged_in")
	item_list = aobj.item_list()
	item = aobj.get_cart()
	
	return render_template("user/menu.html", item_list=item_list, item=item)


@app.route("/add-cart", methods=['GET', 'POST'])
def add_Cart():
	aobj = UserMenu()
	aobj.add_cart(request.form)
	return redirect("/menu")
