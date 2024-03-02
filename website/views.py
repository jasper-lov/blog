from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Post

views = Blueprint('views', __name__)

# NEVER DO THIS (EVER)
# posts = []

@views.route('/', methods=['GET', 'POST'])
def home():

    if request.method == "POST":
        user_input = request.form.get('item')
        new_post = Post(data=user_input)

        db.session.add(new_post)
        db.session.commit()

    posts = list(db.session.query(Post).all())
    return render_template("home.html", posts=posts)

@views.route('/remove/<string:post_id>', methods=['GET'])
def remove(post_id):
    post = db.session.query(Post).filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()
    
    return redirect(url_for('views.home'))

@views.route('/login')
def login():
    return "<h1>Login Page</h1>"