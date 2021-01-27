import pytest
import requests


foo2 = "config_bar2"
expect_foo2 = "config_bar2"
expect_foo1 = "config_bar1"
base_url = "https://postman-echo.com"


@pytest.mark.incremental
def test_get_with_params_request():
    global response_body
    url = f"{base_url}/get"
    headers = {"user-agent": "HttpRunner/3.1.4"}
    payload = {"foo1": "bar11", "foo2": "bar21", "sum_v": f'{sum([1, 2])}'}

    response = requests.request("GET", url, params=payload, headers=headers)
    response_body = response.json()

    assert response.status_code == 200, f"status_code: {response.status_code}, reason:{response.reason}"


def test_get_with_params_args_foo1():
    assert response_body['args']['foo1'] == "bar11"


def test_get_with_params_args_foo2():
    assert response_body['args']['foo2'] == "bar21"


def test_get_with_params_args_sum_v():
    assert response_body['args']['sum_v'] == "3"
