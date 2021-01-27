import requests



'''
#base_url = "https://postman-echo.com"
base_url = "https://httpbin.org/get"
request_headers = {'user-agent': 'HttpRunner/3.1.4'}
payload = {"foo1": "bar11", "foo2": "bar21", "sum_v": f'{sum([1, 2])}'}

request = requests.get(base_url, params= payload, headers= request_headers)
response_body = request.json()
print(request)
print(request.status_code)
print(response_body['args']['foo1'])
print(response_body['args']['sum_v'])
print(response_body['args']['foo2'])
'''

foo2 = "config_bar2"
foo1 = "bar12"
foo3 = "bar32"
base_url = "https://postman-echo.com/post"
'''
post_headers = {"user-agent": "HttpRunner/3.1.4", "Content-Type": "text/plain"}
post_data = {"This is expected to be sent back as part of response body": f'{foo1}-{foo2}-{foo3}.'}

post_response = requests.post(base_url, json= post_data, headers= post_headers)
post_response_body = post_response.json()
print(response_body['args']['foo1'])
print(post_response.status_code)
print(post_response_body)
'''

post_headers = {"user-agent": "HttpRunner/3.1.4", "Content-Type": "application/x-www-form-urlencoded"}
form_data = f"foo1={foo1}&foo2={foo2}&foo3={foo3}"
post_response = requests.post(base_url, data= form_data, headers= post_headers)
post_response_body = post_response.json()

print(post_response.status_code)
print(post_response_body)


# foo1=$foo1 & foo2=$foo2& foo3=$foo3
#"foo1": "testcase_ref_bar1",\n        "foo2": "bar23",\n        "foo3": "bar21"\n 
# foo1 value is get from the test call method
#& is just a separator