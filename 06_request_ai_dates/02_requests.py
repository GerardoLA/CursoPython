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



# 2. Con dependecia (request)
import requests

print("\nGET:")
api_posts = " https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_posts)
json_data = response.json()
print(json_data)

# 3. Un POST
print("\nPOST")
api_posts ="https://jsonplaceholder.typicode.com/posts/"
input={
        "title":"Tateiro probando",
        "body": "El Real Madrid a semifinales, ah no, que le eliminó el Arsenal",
        "userId": 1
}
response = requests.post(api_posts, json=input)
print(response.json())

print("\nOtra manera más PRO")
response = requests.post(
    "https://jsonplaceholder.typicode.c/",
    json={
        "title":"Tateiro pro",
        "body": "Había una vez un circo ",
        "userId": 1
    })
print(response.json())
print(response.status_code) # Estado, 201 sería correcta, si le faltará información debería dar otro.

print("\n Hago un try para comprobar fallo(con direccion inexistente)")
print("\nOtra manera más PRO")
try:
    response = requests.post(
        "https://jsonplaceholder.typicode.c/",
        json={
            "title":"Tateiro pro",
            "body": "Había una vez un circo ",
            "userId": 1
        })
    print(response.json())
    print(response.status_code) # Estado, 201 sería correcta, si le faltará información debería dar otro.
except requests.exceptions.RequestException as e:print(f"No se ha podido hacer, error en la solicitud, revisa la información!: {e}")

print("\nPUT") 
response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={
        "title":"Tateiro pro",
        "body": "Había una vez dos circos ",
        "userId": 1
    })
print(response.json())

print("\nPATCH") # A diferencia del PUT aquí no le pasas el objeto entero, sólo pasas la parte que quieres cambiar.
response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={
       "title":"En dos palabras im-presionante!"
    })
print(response.json())

# Usar la API de GPT-4 o de OPENAI; mirar video de Midudev https://www.twitch.tv/videos/2397854000?filter=archives&sort=time


