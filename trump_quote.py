import requests

url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"
response = requests.get(url)
data = response.json()

print(data["message"])
