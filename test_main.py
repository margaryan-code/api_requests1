import requests
import random
import pytest

def new_post():
    body = {
        'userId': 1,
        'title': 'Kim',
        'body': 'Kardashian'
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    return response.json()['id']

@pytest.mark.smoke
def test_get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200, 'Error status code'
    assert len(response.json()) == 100, 'Error data is incorrect'

@pytest.mark.xxx
@pytest.mark.parametrize('post_id', [2,4,6,8])
def test_get_one_post(post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 200, 'Error Status Code'
    assert response.json()['id'] == post_id, 'Error Id is incorrect'



@pytest.mark.smoke
def test_get_comments_by_post():
    post_id = random.randint(1, 100)
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')
    assert response.status_code == 200, 'Error status code'
    comments = response.json()
    post_id_error = 0
    for elem in comments:
        if elem['postId']!= post_id:
            post_id_error = elem['id']
    assert post_id_error == 0, f'Error id = {post_id_error} '


@pytest.mark.regression
def test_create_new_post():
    body = {
        "userId": 1,
        "title": "Hayk",
        "body": "Abelayn Anna"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )


    assert response.status_code == 201, 'Error Status Code'
    assert response.json()['userId'] == 1, 'userId is incorrect'
    assert response.json()['title'] == 'Hayk', 'Title is incorrect'
    assert response.json()['body'] == 'Abelayn Anna', 'Body is incorrect'


@pytest.mark.regression
@pytest.mark.parametrize('id', [1])
def test_put_the_post(id):
    body = {
        "userId": 1,
        "body": "Kim Kardashian"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{id}',
        json=body,
        headers=headers
    )

    print(response.json())

    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['userId'] == 1, 'userID is incorrect'
    assert response.json()['body'] == 'Kim Kardashian', 'body is incorrect'

@pytest.mark.regression
def test_patch_the_post():
    body = {
        "body": "Kim Kardashian"
    }
    headers = {'Content-Type': 'application/json'}
    response1 = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    response2 = requests.patch(
        'https://jsonplaceholder.typicode.com/posts/1',
    json=body,
    headers=headers
    )

    assert response2.status_code == 200, 'Status code is incorrect'
    assert response2.json()['body'] == 'Kim Kardashian', 'body is incorrect'
    assert response1.json()['title'] == response2.json()['title'], 'Title is incorrect'


@pytest.mark.get
@pytest.mark.parametrize('id', [1])
def test_delete_the_post(id):
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{id}')
    assert response.status_code == 200, 'Delete is incorrect'


