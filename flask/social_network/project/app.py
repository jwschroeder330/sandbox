from flask import (Flask,
                    g,
                    flash,
                    render_template,
                    redirect,
                    url_for,
                    abort)
import forms
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import (LoginManager,
                            login_user, #logs in user
                            logout_user,
                            login_required,
                            current_user)

import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = "asldfjalkghhgwiuerqhgjkdhnaasjdfhsalkfaubg"

login_manager = LoginManager()
login_manager.init_app(app) # sets up the login manager for our app
# note: calling this 'login' requires the url be /login
login_manager.login_view = 'login' # if not logged in, redirect them to the login view

# function for login_manager to use to lookup a User
@login_manager.user_loader
def load_user(userid):
    try: # retrieve record from the db
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist: # no record found
        return None

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE # set the database as global
    g.db.connect() # ensure a global db connection
    g.user = current_user  # an object that will find the current user

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close() # close global db connection
    return response

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    # flash(form.validate_on_submit())
    if form.validate_on_submit():  # detects that user has submitted a valid form
        flash("Form Submission Successful.", "success")  # message and message category
        models.User.create_user(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data # shouldn't we hash this?
                )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            # keep things ambiguous to deter hackers
            flash("Your email or password doesn't match!", "error")
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You've been logged in!", "success")
                return redirect(url_for('index'))
            else:
                flash("Your email or password doesn't match!", "error")
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required  # you need to be logged into see this view
def logout():
    logout_user()  # terminate the session - deletes cookie
    flash("You've been logged out. Come back soon!", "success")
    return redirect(url_for('index'))


@app.route('/')
def index():
    stream = models.Post.select().limit(100)
    return render_template('stream.html', stream=stream)


@app.route('/stream')
@app.route('/stream/<username>')
def stream(username=None):
    template = 'stream.html'
    if username and username != current_user.username:
        try:
            # ** case insensitive comparison
            user = models.User.select().where(models.User.username**username).get()
        except models.DoesNotExist:
            abort(404)
        else:
            stream = user.posts.limit(100)
    else:
        # this is our username, our page
        stream = current_user.get_stream().limit(100)
        user = current_user
    if username:
        template = 'user_stream.html'
    return render_template(template, stream=stream, user=user)

@app.route('/new_post', methods=('GET', 'POST'))
@login_required
def post():
    form = forms.PostForm()
    if form.validate_on_submit():
        models.Post.create(
        # g.user is our global user object, which we must get
        user=g.user._get_current_object(),
        content=form.content.data.strip())
        flash("Message posted! Thanks!", "success")
        return redirect(url_for('index'))
    return render_template('post.html', form=form)

@app.route('/post/<int:post_id>')
def view_post(post_id):
    posts = models.Post.select().where(models.Post.id == post_id)
    if posts.count() == 0:
        abort(404)
    return render_template('stream.html', stream=posts)


@app.route('/follow/<username>')
@login_required
def follow(username):
    try:
        to_user = models.User.get(
        ## ** case insensitive search LIKE
        models.User.username**username)
    except models.DoesNotExist:
        abort(404)
    else:
        try:
            models.Relationship.create(
                # get the current logged in user in flask
                from_user=g.user._get_current_object(),
                to_user=to_user
            )
        except models.IntegrityError:
            # trying to follow someone twice
            pass
        else:
            flash("You're now following {}!".format(to_user.username))
    # return us to the page for the user we want to follow
    return redirect(url_for('stream', username=to_user.username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    try:
        to_user = models.User.get(
        ## ** case insensitive search LIKE
        models.User.username**username)
    except models.DoesNotExist:
        abort(404)
    else:
        try:
            models.Relationship.get(
                # get the current logged in user in flask
                from_user=g.user._get_current_object(),
                to_user=to_user
            ).delete.instance()  # delete the instance of relationship
        except models.IntegrityError:
            # trying to follow someone twice
            pass
        else:
            flash("You've unfollowed {}!".format(to_user.username))
    # return us to the page for the user we want to follow
    return redirect(url_for('stream', username=to_user.username))


# anytime a 404 is triggered, we will run this function
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    models.initialize()  # initialize db
    try:
        models.User.create_user(  # create a dummy user using create_user
                username="Jake",
                email="schroeder.marketing@outlook.com",
                password="password",
                admin=True
                )
    except ValueError:
        pass
    app.run(debug=DEBUG, host=HOST, port=PORT)
