import requests

base_url = "https://api.pokemonbattle.ru/v2"
token = "USER_TOKEN" #USER_TOKEN заменить на значение своего токена
request_headers = {
  "Content-Type": "application/json",
  "trainer_token": token
}
url_pokemons = "/pokemons"
url_add_to_pokeball = "/trainers/add_pokeball"

#Создать покемона
request_body_create_pokemon = {
    "name": "Пайтон",
    "photo_id": 2
}

#Изменить покемона
request_body_change_pokemon = {
    "pokemon_id": "205606", #pokemon_id заменить на id своего покемона
    "name": "Python",
    "photo_id": 2
}

#Добавить покемона в покебол
request_body_add_to_pokeball = {
    "pokemon_id": "205606" #pokemon_id заменить на id своего покемона
}

#Отправить запрос - создать покемона:
response = requests.post(url = f"{base_url}{url_pokemons}", headers = request_headers, json = request_body_create_pokemon)
print(response.text)

#Отправить запрос - изменить имя покемона:
response = requests.put(url = f"{base_url}{url_pokemons}", headers = request_headers, json = request_body_change_pokemon)
print(response.text)

#Отправить запрос - добавить покемона в покебол:
response = requests.post(url = f"{base_url}{url_add_to_pokeball}", headers = request_headers, json = request_body_add_to_pokeball)
print(response.text)