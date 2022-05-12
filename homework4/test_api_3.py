import pytest
import requests

status_code_ok = 200


def test_status(default_url_3):
    r = requests.get(default_url_3)

    assert r.status_code == status_code_ok and r.encoding == "UTF-8" and r.headers["Connection"] == "keep-alive"


def test_json(default_url_3):
    r = requests.get(default_url_3 + "posts/1")
    expected_json = {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum"
                "\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }

    assert r.json() == expected_json


@pytest.mark.parametrize("user_id", [0, 'a', 1111111, -1, "#"])
def test_user_id_negative(default_url_3, user_id):
    r = requests.get(default_url_3 + "posts", params={"userId": user_id})

    assert not r.json()


@pytest.mark.parametrize("input_id, output_id", [(-99, "-99"), (99, "99"), (0, "0")])
@pytest.mark.parametrize("input_title, output_title",
                         [("title1", "title1"), (">_<", ">_<"), ("!@#$%", "!@#$%"), ("12345", "12345")])
def test_post_request(default_url_3, input_id, output_id, input_title, output_title):
    r = requests.post(default_url_3 + "posts", data={"title": input_title, "body": "bar", "userId": input_id})
    date_from_site = r.json()

    assert date_from_site["title"] == output_title and date_from_site["body"] == "bar" and \
           date_from_site["userId"] == output_id
