import json

from flask_login import login_required, login_manager, current_user
from flask_security.utils import hash_password, login_user, logout_user, verify_password

from flask import render_template, session, request, redirect, url_for

from controllers.user_controller import get_user_by_email, create_user
from views.api_routes import get_movie_by_title_first, get_movies_by_title
from views.utils.flask_wtf_classes import RegisterForm, LoginForm
from views import app
import json
from data.MongoDB_MongoEngine.db.db_user_role_security import user_datastore

@app.route('/', methods=['GET'])
def index():
    # global movie_search_cache

   # if request.method == 'POST':
    #    search = request.form['search']
     #   movies = get_movies_by_title(search)
      #  return render_template("index.html", movies=movies)
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == "POST":
        create_user(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hash_password(form.password.data)
        )
        return redirect(url_for('signin'))
    return render_template('signup.html', form=form)

@app.route('/search', methods=['POST'])
def search():
    global movie_search_cache
    value = request.values['current_value']

    movie_result = get_movies_by_title(value)

    response = app.response_class(
        response=json.dumps(movie_result),
        status=200,
        mimetype="application/json"
    )

    return response

@app.route("/signout")
def signout():
    logout_user()
    print("Signing out")
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', first_name=current_user.first_name)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = user_datastore.find_user(email=form.email.data)
        if user:
            if verify_password(form.password.data, user.password):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('profile'))
    return render_template('signin.html', form=form)


@app.route('/edit_account')
def edit_account():
    return render_template('edit_account.html')


@app.route('/movie/<title>')
def movie(title):
    movie_information = get_movie_by_title_first(title)
    return render_template('movie.html', movie_information=movie_information)



@app.route('/watchlist')
@login_required
def watchlist():
    return render_template('watchlist.html')

@app.route('/friends')
def friends():
    return render_template("friends.html")


@app.errorhandler(404)
def handler404(_):
    return render_template('404.html')
