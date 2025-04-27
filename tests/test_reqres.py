import requests
from jsonschema import validate
import schemas

url = 'https://reqres.in'

users = "/api/users/"
register = "/api/register"
login = "/api/login"

session = requests.Session()
session.headers.update({
    "x-api-key": "reqres-free-v1"
})

def test_get_single_user():
    user_id = '2'
    response = session.get(url + users + user_id)
    assert response.status_code == 200
    validate(response.json(), schema=schemas.get_single_user)

def test_get_single_not_found():
    user_id = '212'
    response = session.get(url + users + user_id)
    assert response.status_code == 404

def test_post_great_new_user():
    payload = {
        "name" : "nikita",
        "job" : "master"
    }

    response = session.post(url + users, json=payload)
    assert response.status_code == 201
    validate(response.json(), schema=schemas.post_great_new_user)

def test_put_update_user():
    id_user = '2'
    payload = {
        "name" : "klava",
        "job" : "senior"
    }
    response = session.put(url + users + id_user, json=payload)
    assert response.status_code == 200
    validate(response.json(), schema=schemas.put_update_user)

# def test_put_update_users_bad_request():
#     payload = {
#         "name" : "klava",
#         "job" : "senior"
#     }
# По идеи тест должно падать, так как id не указан. Но запрос отрабатывает 200.
#     response = session.put(url + users, json=payload)
#     assert response.status_code == 400

def test_delete_user():
    user_id = '2'
    response = session.delete(url + users + user_id)

    assert response.status_code == 204

def test_post_register_new_user():
    payload = {
        "email" : "eve.holt@reqres.in",
        "password": "qwerty"
    }
    response = session.post(url + register, json = payload)

    assert response.status_code == 200
    validate(response.json(), schema=schemas.post_register_user)

def test_post_register_user_missing_password():
    payload = {"email": "eve.holt@reqres.in"}

    response = session.post(url + register, json=payload)
    assert response.status_code == 400

def test_post_login_user():
    payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
    response = session.post(url + login, json=payload)
    assert response.status_code == 200
    validate(response.json(), schema=schemas.post_login_user)

def test_post_login_user_missing_password():
    payload = {"email": "eve.holt@reqres.in"}

    assert session.post(url + login, json=payload).status_code == 400
