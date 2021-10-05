from flask import Flask, flash, session
from pitho.Config import conn


class AuthorDashboard():
	def get_user(self, type=1):
		db = conn.connection.cursor()
		db.execute("select id,name from users where user_type=%s ", (str(type)))
		data = db.fetchall()
		return data

	def add_item(self, data):
		author_id = session.get("logged_in")
		user_id = data.get("user_id")
		item_name = data.get("item_name")
		item_price = data.get("item_price")
		db = conn.connection.cursor()
		db.execute("insert into shop_items(item_name,item_price,user_id,author_id) values(%s,%s,%s,%s)", (item_name, str(item_price), str(user_id),str(author_id)));
		conn.connection.commit()
		flash("Item Added")
		return False

	def item_list(self, user_id):
		author_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("select * from shop_items where author_id=%s  and user_id=%s order by id desc", (str(author_id), str(user_id)))
		data = db.fetchall()
		return data

	def delete_item(self, id):
		author_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("delete from shop_items where author_id=%s and id=%s", (str(author_id), str(id)))
		conn.connection.commit()
		flash("successfully deleted")
		return True

	def update_item(self, data):
		author_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("update shop_items set payment_rec=%s where id=%s",(data.get('payment_rec'), str(data.get('id'))))
		conn.connection.commit()
		flash("updated")
		return True

	def total_due_amount(self, user_id):
		author_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("select sum(item_price) as total from shop_items where author_id=%s  and user_id=%s  and payment_rec=%s", (str(author_id), str(user_id), 'no'))
		data = db.fetchone()
		if data['total'] is None:
			data = {'total': 0}
		return data
