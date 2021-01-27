import pytest
import requests

foo1 = "bar12"
foo2 = "config_bar2"
foo3 = "bar32"
expect_foo1 = "config_bar1"
expect_foo2 = "config_bar2"
base_url = "https://postman-echo.com"


@pytest.mark.incremental
def test_post_with_raw_text_request():
    global response_body
    url = f"{base_url}/post"
    post_headers = {'user-agent': 'HttpRunner/3.1.4',
                    'Content-Type': 'text/plain'}
    post_data = f"This is expected to be sent back as part of response body: {foo1}-{foo2}-{foo3}."

    response = requests.request(
        "POST", url, json=post_data, headers=post_headers)
    response_body = response.json()

    assert response.status_code == 200, f"status_code: {response.status_code}, reason:{response.reason}"


def test_post_with_raw_text_data():

    assert response_body['data'] == '"This is expected to be sent back as part of response body: bar12-config_bar2-bar32."'


@pytest.mark.incremental
def test_post_form_data_request():
    global post_response_body
    foo2 = "bar23"
    url = f"{base_url}/post"
    form_data = f"foo1={foo1}&foo2={foo2}&foo3={foo3}"
    post_headers = {"user-agent": "HttpRunner/3.1.4",
                    "Content-Type": "application/x-www-form-urlencoded"}

    post_response = requests.post(url, data=form_data, headers=post_headers)
    post_response_body = post_response.json()

    assert post_response.status_code == 200, f"status_code: {post_response.status_code}, reason:{post_response.reason}"


def test_post_form_data_foo1():
    assert post_response_body['form']['foo1'] == expect_foo1


def test_post_form_data_foo2():
    assert post_response_body['form']['foo2'] == "bar23"


def test_post_form_data_foo3():
    assert post_response_body['form']['foo3'] == "bar21"
