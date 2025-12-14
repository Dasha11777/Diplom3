
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IngredientModalPage(BasePage):
    MODAL = (By.XPATH, "//section[.//h2[normalize-space()='Детали ингредиента']]")
    CLOSE_BTN = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    TITLE = (By.XPATH, ".//h2[normalize-space()='Детали ингредиента']")
    INGREDIENT_NAME = (By.XPATH, "//section[.//h2[normalize-space()='Детали ингредиента']]//p[contains(@class, 'text_type_main-medium')]")

    def is_open(self):
        # Проверяем текущее состояние модалки без ожидания
        elements = self.find_elements_now(self.MODAL)
        return len(elements) > 0 and elements[0].is_displayed()

    def wait_until_open(self):
        """Ждём, пока модалка откроется"""
        self.wait_for_visible_elements(self.MODAL)

    def get_title(self):
        return self.get_text_with_wait(self.TITLE)

    def get_ingredient_name(self):
        """Получаем имя ингредиента из модального окна"""
        return self.get_text_with_wait(self.INGREDIENT_NAME)

    def close(self):
        # Кликаем на кнопку закрытия (метод уже ждёт кликабельности)
        self.click_with_wait(self.CLOSE_BTN)
        # Ждём, пока модалка исчезнет
        self.wait_for_element_invisible(self.MODAL)
