from pitho import app
from pitho.models.user.model_dashboard import UserDashboard
from flask import render_template, request, session, redirect


@app.route("/dashboard", methods=['GET', 'POST'])
def user_dashboard():
	aobj = UserDashboard()
	if session.get("logged_in") is None:
		return redirect("/")
	if session.get("user_type") == 2:
		return redirect("/author-dashboard")
	id = session.get("logged_in")
	item_list = aobj.item_list()
	total = aobj.total_due_amount()
	return render_template("user/dashboard.html", item_list=item_list, total=total)

