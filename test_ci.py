import requests
import pytest # have to install via command "pip3 install -U pytest"

def test_health_check():
    r = requests.get('http://localhost:8085')
    assert(r.status_code == 404)

def test_hello_world():
    r = requests.get('http://localhost:8085/hello-world')
    assert(r.status_code == 200)

def test_hello_world_with_name():
    name = "Michael"
    r = requests.get('http://localhost:8085/hello-world', params={"name": name})
    body = r.json()
    assert(body["content"] == f"Hello, {name}!")
