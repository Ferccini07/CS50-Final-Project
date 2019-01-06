from flask import render_template, url_for, flash, redirect
# After we have Package Structured the app, we have to add package name and then
# the moodule name. final_project.forms
from final_project import app, db, bcrypt
from final_project.forms import RegistrationForm, LoginForm
from final_project.models import User, Post

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

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', imena=imena)

@app.route('/movie')
def movie():
    title = "Movie Info App-Final Project CS50 | Movie Details"
    return render_template('movie.html', title=title, imena=imena)

@app.route('/register', methods=['GET', 'POST'])
def register():
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
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You are successfully Loged In!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Unsuccessful Login. Username/Password not correct.', 'danger')
    return render_template('login.html', title="Login", form=form)