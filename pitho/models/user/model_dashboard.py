from flask import Flask, flash, session
from pitho.Config import conn


class UserDashboard():
	def item_list(self):
		user_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("select * from shop_items where user_id=%s order by id desc", (str(user_id)))
		data = db.fetchall()
		return data

	def total_due_amount(self):
		user_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("select sum(item_price) as total from shop_items where user_id=%s and payment_rec=%s", (str(user_id), 'no'))
		data = db.fetchone()
		
		if data['total'] is None:
			data = {'total': 0}
		return data
