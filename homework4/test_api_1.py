import requests
import cerberus
import pytest


def test_status(default_url_1):
    r = requests.get(default_url_1)

    assert r.status_code == 200 and r.encoding == "UTF-8" and r.headers["Connection"] == "keep-alive"


def test_json(default_url_1):
    r = requests.get(default_url_1 + "api/breeds/image/random")
    expected_json = {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
    validate = cerberus.Validator()

    assert validate(r.json(), expected_json)


def test_update_response_json(default_url_1):
    r = requests.get(default_url_1 + "api/breeds/image/random")
    r_old = dict(r.json())
    r = requests.get(default_url_1 + "api/breeds/image/random")
    r_new = dict(r.json())

    assert r_old != r_new


@pytest.mark.parametrize("expected_breed", ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"])
def test_content_json(default_url_1, expected_breed):
    res = requests.get(default_url_1 + "api/breed/hound/list")
    date_from_site = res.json()["message"]

    assert expected_breed in date_from_site


@pytest.mark.parametrize("dog,breed", [("wolfhound", ["irish"]),
                                       ("springer", ["english"]),
                                       ("sheepdog", ["english",
                                                     "shetland"]),
                                       ("papillon", []),
                                       ("komondor", [])],
                         ids=["wolfhound", "springer", "sheepdog", "papillon", "komondor"])
def test_content_json_all(default_url_1, dog, breed):
    r = requests.get(default_url_1 + 'api/breeds/list/all')
    date_from_site = r.json()["message"][dog]

    assert date_from_site == breed
