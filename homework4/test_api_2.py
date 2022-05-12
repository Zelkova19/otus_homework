import requests
import cerberus
import pytest


def test_status(default_url_2):
    r = requests.get(default_url_2)

    assert r.status_code == 200 and r.encoding == "UTF-8" and r.headers["Content-Encoding"] == "gzip"


def test_validate_json(default_url_2):
    r = requests.get(default_url_2 + "breweries/amadtree-brewing-cincinnati")
    expected_json = {
        "message": {"type": "string"}
    }
    validate = cerberus.Validator()

    assert validate(r.json(), expected_json)


def test_update_response_json(default_url_2):
    r = requests.get(default_url_2 + "breweries/amadtree-brewing-cincinnati")
    r_old = dict(r.json())
    r = requests.get(default_url_2 + "breweries/amadtree-brewing-cincinnati")
    r_new = dict(r.json())

    assert r_old == r_new


@pytest.mark.parametrize("key", ["id", 'name'],
                         ids=["id", "name"])
def test_variability_keys(default_url_2, key):
    r = requests.get(default_url_2 + "breweries?by_dist=38.8977,77.0365")
    count = len(r.json())
    id_list = set()
    for i in r.json():
        id_list.add(i[key])

    assert len(id_list) == count


@pytest.mark.parametrize("expected_name",
                         ["Banjo Brewing", "Dirt Road Brewing", "Dented Face Brewing Company", "Bent Shovel Brewing"])
def test_content_json_all(default_url_2, expected_name):
    r = requests.get(default_url_2 + "breweries")
    date_from_site = r.json()
    name_list = set()
    for i in date_from_site:
        name_list.add(i["name"])

    assert expected_name in name_list
