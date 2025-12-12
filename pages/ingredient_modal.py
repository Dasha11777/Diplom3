
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage

class IngredientModal(BasePage):
    # Универсальные локаторы для модального окна
    MODAL = (By.XPATH, "//section[contains(@class, 'Modal') or @class='modal']")
    CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'close') or @aria-label='Закрыть']")
    TITLE = (By.XPATH, "//h2 | //div[contains(@class, 'Modal')]//h2")

    def is_open(self):
        try:
            time.sleep(0.5)  # Даём время на появление модалки
            elements = self.driver.find_elements(*self.MODAL)
            # Проверяем, что элемент не только существует, но и виден
            if len(elements) > 0:
                return elements[0].is_displayed()
            return False
        except:
            return False

    def get_title(self):
        return self.find(self.TITLE).text

    def close(self):
        try:
            # Пробуем найти и нажать кнопку закрытия
            close_button = self.wait.until(EC.element_to_be_clickable(self.CLOSE_BTN))
            close_button.click()
            time.sleep(1)
        except:
            # Если не получилось, пробуем нажать Escape или кликнуть по overlay
            try:
                from selenium.webdriver.common.keys import Keys
                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
                time.sleep(1)
            except:
                pass
