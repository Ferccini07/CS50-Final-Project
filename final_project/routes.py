import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
# After we have Package Structured the app, we have to add package name and then
# the moodule name. final_project.forms
from final_project import app, db, bcrypt
from final_project.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from final_project.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/commentary')
def commentary():
    title = 'Commentary'
    posts = Post.query.all()
    return render_template('commentary.html', title=title, posts=posts)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie')
def movie():
    title = "Movie Info App-Final Project CS50 | Movie Details"
    return render_template('movie.html', title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('commentary'))
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
        return redirect(url_for('commentary'))
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
            return redirect(next_page) if next_page else redirect(url_for('commentary'))
        else:
            flash('Unsuccessful Login. Username/Password not correct.', 'danger')
    return render_template('login.html', title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

# Saving picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    # using the same file extention user uesed. this code makes sure it happens
    # this underscore variable will not be used
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    # this line will join full root file path with 'static...' and with picture filename
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    picture_pathRplc = picture_path.replace('\\', '/')
    # saving the picture at picture_path
    
    # Resizing the picture
    output_size = (128, 128)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    # Saving resized picture
    i.save(picture_pathRplc)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file =  url_for('static', filename='profile_pics/' + current_user.image_file)
    title = 'Account'
    return render_template('account.html', title=title, 
                            current_user=current_user, image_file=image_file, form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    title = 'New Movie'
    legend = 'New Post'
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content = form.content.data, 
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('New comment has been created!', 'success')
        return redirect(url_for('commentary'))
    return render_template('create_post.html', title=title,
                            form=form, legend = legend)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    title = 'Update Post'
    legend = 'Update Post'
    if post.author != current_user:
        # forbidden route
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        # Populating form with values
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title=post.title, 
                        form=form, legend = legend)

@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_comment(post_id):
    post = Post.query.get_or_404(post_id)
    title = 'Update Post'
    legend = 'Update Post'
    if post.author != current_user:
        # forbidden route
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted.', 'success')
    return redirect(url_for('commentary'))