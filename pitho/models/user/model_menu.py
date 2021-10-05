from flask import Flask, flash, session
from pitho.Config import conn


class UserMenu():
	def item_list(self):
		user_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("select * from item_list order by id desc")
		data = db.fetchall()
		return data

	def add_cart(self, data):
		user_id = session.get("logged_in")
		db = conn.connection.cursor()
		id = data.get("id")
		quantity = data.get("quantity")
		db.execute("insert into cart_items(user_id,item_id,quantity) values(%s,%s,%s)", (str(user_id), str(id), str(quantity)))
		conn.connection.commit()
		return data

	def get_cart(self):
		user_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("select count(*) as cnt from cart_items where user_id=%s", (str(user_id)))
		data = db.fetchone()
		if data is not None:
			return data['cnt']
		return '0'
