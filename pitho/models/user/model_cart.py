from flask import Flask, session, flash
from pitho.Config import conn


class Cart():
	def cart_items(self):
		user_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("SELECT c.id, s.item_name, s.item_price,c.quantity from item_list as s join cart_items as c on c.item_id = s.id where c.user_id=%s", (str(user_id)))
		data = db.fetchall()
		return data

	def delete_cartitem(self, id):
		user_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("delete from cart_items where user_id=%s and id=%s", (str(user_id), str(id)))
		conn.connection.commit()
		flash("successfully deleted")		
		return True
