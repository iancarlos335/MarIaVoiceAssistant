import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"
# endpoint = "http://localhost:8000/iaresponse/audio/"

get_response = requests.post(endpoint, json={"title": "hello"})
# print(get_response.text) # prints raw text response
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict
print(get_response.json())
