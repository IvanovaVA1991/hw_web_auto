# Написать тест с использованием pytest и requests, в котором:
# Адрес сайта, имя пользователя и пароль хранятся в config.yaml
# conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login с передачей параметров “username" и "password" и возвращающей токен авторизации
# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого пользователя, для этого выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c хедером, содержащим токен авторизации в параметре "X-Auth-Token". Для отображения постов другого пользователя передается "owner": "notMe".
# http://restapi.adequateshop.com/api/authaccount/registration
# http://restapi.adequateshop.com/api/authaccount/login
# Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется его наличие на сервере по полю «описание».
# Подсказка: создание поста
# выполняется запросом к https://test-stand.gb.ru/api/posts с передачей параметров title, description, content.

import requests
import yaml


with open('config.yaml') as f:
    data1 = yaml.safe_load(f)


def token_auth(token):
    response = requests.get(url=data1['url1'], headers={'X-Auth-Token': token}, params={"owner": "notMe"})  #get запрос c хедером, содержащим токен авторизации в параметре "X-Auth-Token"
    #Для отображения постов другого пользователя передается "owner": "notMe".
    conten_var = [item['content'] for item in response.json()['data']]   # через генератор создали список постов (сам контент)
    return conten_var  #возвращаем список постов
    #return response.json()[data]   # возвращаем список с данными


def test_step2(login):
    assert 'Домашнее задание №1' in token_auth(login)


def test_step3(login):
    obj_data = requests.post(url=data1['url'], data={'username': data1['username'], 'password': data1['password']})
    token = obj_data.json()['token']
    post = requests.post(url=data1['url1'], headers={'X-Auth-Token': token}, params={'title': data1['title'], 'description': data1['description'], 'content': data1['content']})
    my_post = post.json()['description']
    assert 'beautiful' in my_post



