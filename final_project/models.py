from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from final_project import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# class 'User' (it has to inherit from both Model class and UserMixin)
# UserMixin provides default implementations for the methods that
# Flask-Login expects user objects to have.
# 'Model' is a class provided by SQLAlchemy object 'db'
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    # 'posts' atribute has a relationship with a 'Post' model
    # 'backref' is similar to adding another column to 'Post' model
    # When we have a post we can use author attribute to get user who created post
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        # dumps creates a JSON Web Signature
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    # with this we are telling python not to expect the 'self' parameter
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            # loads - Reverse of dumps(), raises BadSignature if the signature validation fails
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


    # How this object will be printed
    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    # ForeignKey - it has a relationship with User Model
    # lowercase 'u' in 'user.id' below is because in the User model the 'Post' class is referenced
    # and here are table and column names referenced
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


