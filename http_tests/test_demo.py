import test_json

import requests
from jsonpath import jsonpath
from hamcrest import *
from jsonschema import validate


class TestDemo:
    def test_get(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "yang"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "yang"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get("https://httpbin.testing-studio.com/get", headers={"h": "header demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["headers"]["H"] == "header demo"

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "yang"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]["name"] == "yang"

    def test_hogwarts_json(self):
        r =requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["category_list"]["categories"][2]["name"] == "职位内推"

    def test_hogwarts_jsonpath(self):
        r =requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert jsonpath(r.json(), "$..name")[2] == "职位内推"

    def test_hamcrest(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert_that(jsonpath(r.json(), "$..name")[2], equal_to("职位内推"))

    def test_get_login_jsonschema(self):
        url = "https://ceshiren.com/categories.json"
        data = requests.get(url, params={"limit": "2"}).json()
        schema = test_json.load(open("topic_schema.json"))
        validate(data, schema=schema)
