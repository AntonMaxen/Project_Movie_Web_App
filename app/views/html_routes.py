from views import app
from flask import render_template, session


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/create_account')
def create_account():
    return render_template('create_account.html')


@app.route('/edit_account')
def edit_account():
    return render_template('edit_account.html')


@app.route('/friends')
def friends():
    return render_template("friends.html")


@app.errorhandler(404)
def handler404(_):
    return render_template('404.html')
