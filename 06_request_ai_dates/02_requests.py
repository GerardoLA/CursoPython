# Cómo hacer peticiones API con Python
# Con o sin dependencias

# Sin dependencias
import urllib.error
import urllib.request
import json


api_posts = "https://jsonplaceholder.typicode.com/posts/"
try:
    response = urllib.request.urlopen(api_posts)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
    response.close()
except urllib.error.URLError as e:
    print(f"Error en la solicitud: {e}")

# Con dependecia (request)
import requests

print("\nGET:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_posts)
json = response.json()
print(json[0])

