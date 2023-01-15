from main import app


def test_api_posts():
    response = app.test_client().get('/api/posts')
    print(response.status_code)
    print(response.data)


def test_api_posts_id():
    response = app.test_client().get('/api/posts/1')
    print(response.data)
