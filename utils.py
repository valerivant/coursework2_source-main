import json


def get_post_all():
    with open('data\\posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def get_posts_by_user(user_name):
    user_list = [user for user in get_post_all() if user_name.lower() == user['poster_name']]
    return user_list


def get_comments_by_post_id(post_id):
    with open('data\\comments.json', 'r', encoding='utf-8') as file:
        comments = json.load(file)
        comment_list = [comment for comment in comments if post_id == comment['post_id']]
        return comment_list


def search_for_posts(query):
    posts = [post for post in get_post_all() if query.lower() in post['content']]
    return posts


def get_post_by_pk(pk):
    for post in get_post_all():
        if pk == post['pk']:
            return post
