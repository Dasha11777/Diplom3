
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Методы с явным ожиданием (используют WebDriverWait)
    
    def wait_for_visible_element(self, locator):
        """Ожидание: дождаться видимости элемента и вернуть его"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_visible_elements(self, locator):
        """Ожидание: дождаться видимости всех элементов и вернуть их"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_for_clickable_element(self, locator):
        """Ожидание: дождаться кликабельности элемента и вернуть его"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_in_dom(self, locator):
        """Ожидание: дождаться появления элемента в DOM (может быть невидимым)"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_elements_in_dom(self, locator):
        """Ожидание: дождаться появления элементов в DOM (могут быть невидимыми)"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_element_invisible(self, locator):
        """Ожидание: дождаться исчезновения элемента (невидимость или отсутствие в DOM)"""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def click_with_wait(self, locator):
        """Ожидание + действие: дождаться кликабельности и кликнуть на элемент"""
        element = self.wait_for_clickable_element(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            # Если обычный клик не сработал, используем JavaScript
            self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element_with_wait(self, locator):
        """Ожидание + действие: дождаться элемента в DOM и прокрутить до него"""
        element = self.wait_for_element_in_dom(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def get_text_with_wait(self, locator):
        """Ожидание + получение: дождаться видимости элемента и получить его текст"""
        return self.wait_for_visible_element(locator).text

    # Методы без ожидания (мгновенный поиск)
    
    def find_element_now(self, locator):
        """Без ожидания: найти элемент немедленно (может не существовать или быть невидимым)"""
        return self.driver.find_element(*locator)

    def find_elements_now(self, locator):
        """Без ожидания: найти все элементы немедленно (может вернуть пустой список)"""
        return self.driver.find_elements(*locator)

    # Вспомогательные методы
    
    def open(self, url):
        """Открыть URL в браузере"""
        self.driver.get(url)

    def execute_script(self, script, *args):
        """Выполнить JavaScript код в контексте текущей страницы"""
        return self.driver.execute_script(script, *args)

    def send_keys_to_body(self, keys):
        """Отправить нажатия клавиш элементу body (для глобальных горячих клавиш)"""
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(keys)
