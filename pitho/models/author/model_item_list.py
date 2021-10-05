from flask import Flask, flash, session
from pitho.Config import conn


class ItemList():
	def add_list(self, data):
		author_id = session.get("logged_in")
		item_name = data.get("item_name")
		item_price = data.get("item_price")
		db = conn.connection.cursor()
		db.execute("insert into item_list(item_name,item_price,author_id) values(%s,%s,%s)", (item_name, str(item_price), str(author_id)))
		db.connection.commit()
		flash("item added")
		return False

	def item_list(self):
		author_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("select * from item_list where author_id=%s order by id desc", (str(author_id)))
		data = db.fetchall()
		return data

	def delete(self, id):
		author_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("delete from item_list where author_id=%s and id=%s", (str(author_id), str(id)))
		conn.connection.commit()
		flash("successfully deleted")
		return True

	def item(self, id):
		author_id = session.get("logged_in")
		db = conn.connection.cursor()
		db.execute("select * from item_list where author_id=%s and item_name like %s", (str(author_id), '%'+str(id)+'%'))
		data = db.fetchall()
		htmldata = ''
		for obj in data:
			htmldata += '<li data-id="'+str(obj['item_price'])+'">'+obj['item_name']+'</li>'
		return htmldata
