from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *
from model import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route("/")
def home():
   return render_template("home.html" )
	
@app.route("/play")
def play():
	return render_template("play.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
	error= None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
			return render_template("home.html")
		else:
			return render_template("portal.html" )
	else:
		return render_template('login.html', error=error)


@app.route('/portal' ,  methods=['GET', 'POST'])
def portal_add():
	if request.method == 'GET':
		name =request.form["name"]
		score = request.form["score"]
		time= request.form["time"]
		portal_add(name, score, time)
		return render_template("play.html")


if __name__ == '__main__':
	app.run(debug=True)