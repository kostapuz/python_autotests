import requests
import pytest

base_url = 'https://api.pokemonbattle.ru/v2'
token = "USER_TOKEN" #USER_TOKEN заменить на значение своего токена
trainer_id = "USER_TRAINER_ID" #USER_TRAINER_ID заменить на id своего тренера
request_headers = {
  "Content-Type": "application/json",
  "trainer_token": token
}
url_get_trainers = "/trainers"
request_body_create_pokemon = {
    "name": "Пайтон",
    "photo_id": 2
}

#Получить список тренеров
def test_status_code():
    response = requests.get(url = f"{base_url}{url_get_trainers}", headers = request_headers)
    assert response.status_code == 200

#Ответ содержит поле с именем тренера
def test_response_includes_trainer_id():
    response_get = requests.get(url = f"{base_url}{url_get_trainers}", params = {"trainer_id": trainer_id}, headers = request_headers)
    assert response_get.json()["data"][0]["trainer_name"] == "TRAINER_NAME" #TRAINER_NAME заменить на имя своего тренера 