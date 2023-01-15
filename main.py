import requests
from flask import Flask, render_template, request, jsonify

import logging

from utils import get_post_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user

logging.basicConfig(level=logging.INFO, filename="logs/api.log", filemode="w",
                    format="%(asctime)s [%(levelname)s] %(message)s")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.get('/')
def index():
    return render_template('index.html', items=get_post_all())


@app.get('/posts/<int:post_id>')
def page_id(post_id):
    comments = get_comments_by_post_id(post_id)
    len_comments = len(comments)
    return render_template('post.html', item=get_post_by_pk(post_id), comments=comments, len_comments=len_comments)


@app.get('/users/<username>')
def page_users(username):
    return render_template('user-feed.html', items=get_posts_by_user(username))


@app.get('/search')
def search_page():
    search = request.args.get('s')
    items = search_for_posts(search)
    len_post = len(items)
    return render_template('search.html', items=items, search=search, len_post=len_post)


@app.errorhandler(404)
def page_not(error):
    return "<h1><center>404<br>PAGE NOT FOUND</center></h1>", 404


@app.errorhandler(500)
def server_error(error):
    return "<h1><center>500<br>INTERNAL SERVER ERROR</center></h1>", 500


@app.route('/api/posts')
def api_posts():
    posts_list = []
    for post in get_post_all():
        posts_list.append(post)
    return jsonify(posts_list)


@app.route('/api/posts/<int:post_id>')
def api_posts_id(post_id):
    post = get_post_by_pk(post_id)
    return jsonify(post)


if __name__ == '__main__':
    app.run(debug=True)
