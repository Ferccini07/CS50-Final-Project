from flask import render_template, url_for, flash, redirect, request
# After we have Package Structured the app, we have to add package name and then
# the moodule name. final_project.forms
from final_project import app, db, bcrypt
from final_project.forms import RegistrationForm, LoginForm
from final_project.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

imena = [
    {
        'ime': 'Borna',
        'prezime': 'Fercec'
    },
        {
        'ime': 'Miro',
        'prezime': 'Hunjak'
    }
]


@app.route('/home')
def home():
    title = 'Home'
    # user = User.query.filter_by(username).first() 
    return render_template('home.html', title=title)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/movie')
def movie():
    title = "Movie Info App-Final Project CS50 | Movie Details"
    return render_template('movie.html', title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hashing password and making it secure
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Creating user by passing username and email from form and hashed password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # adding user to db
        db.session.add(user)
        db.session.commit()
        flash(f'Account for {form.username.data} is successfully created!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # user.password is from db and second is from form
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # form.remember.data is a true/false value. if user checks it its true
            login_user(user, remember=form.remember.data)
            # this line will get the account page when user loggs in
            # args is a dictionary but we will not access it this way ,next is parameter from url
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Unsuccessful Login. Username/Password not correct.', 'danger')
    return render_template('login.html', title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/account")
@login_required
def account():
    title = 'Account'
    return render_template('account.html', title=title, current_user=current_user)