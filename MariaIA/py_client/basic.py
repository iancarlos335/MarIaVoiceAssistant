import requests

endpoint = "http://127.0.0.1:8000/api"

get_response = requests.get(endpoint, json={"test": "hello world"})
print(get_response.json())