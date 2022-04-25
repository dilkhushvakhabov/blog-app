from flask import Flask, render_template
from db import get_posts

app = Flask(__name__)


@app.route('/')
def index_view():
    return render_template('index.html', ppp=get_posts(), name='Aziz')


@app.route('/<int:pk>')
def post_detail_view(pk):
    return render_template('post_detail.html')

