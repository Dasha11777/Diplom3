import requests
import allure

from urls import Urls

BASE_URL = Urls.BASE_URL + "api"

class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL

    @allure.step("Создание пользователя через API")
    def create_user(self, user_data):
        return requests.post(f"{self.base_url}/auth/register", json=user_data)

    @allure.step("Логин пользователя через API")
    def login(self, login_data):
        return requests.post(f"{self.base_url}/auth/login", json=login_data)

    @allure.step("Удаление пользователя через API")
    def delete_user(self, token):
        headers = {'Authorization': token}
        return requests.delete(f"{self.base_url}/auth/user", headers=headers)

    @allure.step("Получение списка ингредиентов через API")
    def get_ingredients(self):
        return requests.get(f"{self.base_url}/ingredients")
