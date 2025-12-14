import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

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

