from flask import Flask, render_template
from db import get_posts, get_post

app = Flask(__name__)


@app.route('/')
def index_view():
    print('hello world')
    return render_template('index.html', ppp=get_posts(), name='Aziz')


@app.route('/<int:pk>/')
def post_detail_view(pk):
    post = get_post(pk)
    return render_template('post_detail.html', post=post)

