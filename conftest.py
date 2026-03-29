import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from api_client import ApiClient
import random
import string

from urls import Urls

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1240,756")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1240")
        firefox_options.add_argument("--height=756")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise Exception(f"Browser {browser} not supported")
    
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def api_client():
    """Фикстура для API клиента"""
    return ApiClient()

@pytest.fixture(scope="function")
def authorized_user(driver, api_client):
    """
    Фикстура создает пользователя через API, авторизует его в браузере
    и удаляет после завершения теста
    """
    # Генерируем случайные данные пользователя
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    user_data = {
        "email": f"test_{random_suffix}@test.com",
        "password": "password123",
        "name": f"TestUser_{random_suffix}"
    }
    
    # Создаем пользователя через API
    response = api_client.create_user(user_data)
    assert response.status_code == 200, f"Не удалось создать пользователя: {response.text}"
    
    response_data = response.json()
    access_token = response_data['accessToken']
    refresh_token = response_data.get('refreshToken', '')
    
    # Авторизуем пользователя в браузере через localStorage
    driver.get(Urls.BASE_URL)
    
    # Сохраняем оба токена в localStorage
    driver.execute_script(f"localStorage.setItem('accessToken', '{access_token}');")
    if refresh_token:
        driver.execute_script(f"localStorage.setItem('refreshToken', '{refresh_token}');")
    driver.refresh()
    
    yield {"user_data": user_data, "token": access_token}
    
    # Удаляем пользователя после теста
    api_client.delete_user(access_token)

