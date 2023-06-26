import requests

endpoint = "https://httpbing.org/status/200/"
endpoint = "https://httpbing.org/"

get_response = requests.get(endpoint)
print(get_response.text)