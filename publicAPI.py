import requests

response = requests.get("https://coffee.alexflipnote.dev/random.json")

print(response.json())