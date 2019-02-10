import json
from final_project.models import Post
from final_project import db
'''This functions runs only once to get the posts from 'posts.json' into db'''
# declaring a decorator that makes sure function runs only once
# so that the 'posts.json' file is loaded only once
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

@run_once
def json_to_post():
    with open('final_project/posts.json') as f:
        data = json.load(f)
    
    for element in data:
        post = Post(title=element['title'], content=element['content'], user_id=element['user_id'])
        db.session.add(post)
        db.session.commit()

    return(Post.query.all())
    