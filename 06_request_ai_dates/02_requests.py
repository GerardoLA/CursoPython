# Cómo hacer peticiones API con Python
# Con o sin dependencias

# Sin dependencias
import urllib.error
import urllib.request
import json

api_posts = "https://pokeapi.co/api/v2/pokemon-species/aegislash"
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(api_posts, headers=headers)
try:
    response = urllib.request.urlopen(req)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
    response.close()
except urllib.error.URLError as e:
    print(f"Error en la solicitud: {e}")



# Con dependecia (request)
import requests

print("\nGET:")
api_posts = " https://pokeapi.co/api/v2/berry/"
response = requests.get(api_posts)
json_data = response.json()
print(json_data.keys())
results = json_data["results"]
for i in range(0,10):
    print(f"{i +1} : {results[i]}")

# 3. Un POST
print("\nPOST")
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts/",
    json={
        "title":"foo",
        "body": "bar",
        "userId": 1
    })
print(response.status_code)


