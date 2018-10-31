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
                            login_user,
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
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
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
    if form.validate_on_submit():
        flash("Form Submission Successful.", "success")
        models.User.create_user(
                email=form.email.data,
                password=form.password.data
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
@login_required
def logout():
    logout_user()
    flash("You've been logged out. Come back soon!", "success")
    return redirect(url_for('index'))


@app.route('/')
def index():
    tacos = models.Taco.select().limit(10)
    return render_template('index.html', tacos=tacos)
  
@app.route('/taco', methods=('GET', 'POST'))
def taco():
    form = forms.TacoForm()
    if form.validate_on_submit():
        flash("Form Submission Successful.", "success")
        models.Taco.create_taco(
                user=g.user._get_current_object(),
                protein=form.protein.data,
                shell=form.shell.data,
                cheese=form.cheese.data,
                extras=form.extras.data)
        return redirect(url_for('index'))
    flash("Something went wrong, please try again.")
    return render_template('taco.html', form=form)
  
  
if __name__ == '__main__':
    models.initialize()
    models.Taco.delete()
    try:
        # create dummy test user
        models.User.create_user(
                email="jschroeder@linkmedia360.com",
                password="password"
                )
    except ValueError:
        pass
    app.run(debug=DEBUG, host=HOST, port=PORT)








