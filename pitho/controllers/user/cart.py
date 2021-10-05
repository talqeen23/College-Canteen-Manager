from pitho import app
from pitho.models.user.model_cart import Cart
from flask import render_template, session, redirect, request


@app.route("/cart",methods=['GET', 'POST'])
def shop_cart():
	aobj = Cart()
	if session.get("logged_in") is None:
		return redirect("/")
	id = session.get("logged_in")
	cart_items = aobj.cart_items()
	return render_template("user/cart.html",item_list=cart_items)


@app.route("/cart/delete/<id>/",methods=['GET', 'POST'])
def delete_cartitem(id):
	aobj = Cart()
	aobj.delete_cartitem(id)
	return redirect("/cart")


def checkout(id):
	return redirect("/menu")
