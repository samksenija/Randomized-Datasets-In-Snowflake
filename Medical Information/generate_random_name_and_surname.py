#Random name and surname generator using the Random User API
import requests

response = requests.get("https://randomuser.me/api/?inc=name")
data = response.json()

name = data["results"][0]["name"]["first"]
surname = data["results"][0]["name"]["last"]
