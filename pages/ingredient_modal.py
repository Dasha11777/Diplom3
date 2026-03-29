import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IngredientModalPage(BasePage):
    MODAL = (By.XPATH, "//section[.//h2[normalize-space()='Детали ингредиента']]")
    CLOSE_BTN = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    TITLE = (By.XPATH, ".//h2[normalize-space()='Детали ингредиента']")
    INGREDIENT_NAME = (By.XPATH, "//section[.//h2[normalize-space()='Детали ингредиента']]//p[contains(@class, 'text_type_main-medium')]")
    INGREDIENT_IMAGE = (By.XPATH, "//section[.//h2[normalize-space()='Детали ингредиента']]//img")

    CALORIES = (By.XPATH, "//section[.//h2[normalize-space()='Детали ингредиента']]//p[contains(text(), 'Калории')]/following-sibling::p[@class]")
    PROTEINS = (By.XPATH, "//section[.//h2[normalize-space()='Детали ингредиента']]//p[contains(text(), 'Белки')]/following-sibling::p[@class]")
    FATS = (By.XPATH, "//section[.//h2[normalize-space()='Детали ингредиента']]//p[contains(text(), 'Жиры')]/following-sibling::p[@class]")
    CARBS = (By.XPATH, "//section[.//h2[normalize-space()='Детали ингредиента']]//p[contains(text(), 'Углеводы')]/following-sibling::p[@class]")

    @allure.step('Проверка открытия модального окна ингредиента')
    def is_open(self):
        # Проверяем текущее состояние модалки без ожидания
        elements = self.find_elements_now(self.MODAL)
        return len(elements) > 0 and elements[0].is_displayed()

    @allure.step('Ожидание открытия модального окна ингредиента')
    def wait_until_open(self):
        """Ждём, пока модалка откроется"""
        self.wait_for_visible_elements(self.MODAL)

    @allure.step('Получение заголовка модального окна ингредиента')
    def get_title(self):
        return self.get_text_with_wait(self.TITLE)

    @allure.step('Получение имени ингредиента из модального окна')
    def get_ingredient_name(self):
        """Получаем имя ингредиента из модального окна"""
        return self.get_text_with_wait(self.INGREDIENT_NAME)

    @allure.step('Проверка наличия изображения ингредиента')
    def has_image(self):
        """Проверяем, что изображение ингредиента присутствует"""
        elements = self.find_elements_now(self.INGREDIENT_IMAGE)
        return len(elements) > 0 and elements[0].is_displayed()

    @allure.step('Получение калорийности ингредиента')
    def get_calories(self):
        """Получаем калорийность ингредиента"""
        return self.get_text_with_wait(self.CALORIES)

    @allure.step('Получение количества белков')
    def get_proteins(self):
        """Получаем количество белков"""
        return self.get_text_with_wait(self.PROTEINS)

    @allure.step('Получение количества жиров')
    def get_fats(self):
        """Получаем количество жиров"""
        return self.get_text_with_wait(self.FATS)

    @allure.step('Получение количества углеводов')
    def get_carbs(self):
        """Получаем количество углеводов"""
        return self.get_text_with_wait(self.CARBS)

    @allure.step('Закрытие модального окна ингредиента')
    def close(self):
        # Кликаем на кнопку закрытия (метод уже ждёт кликабельности)
        self.click_with_wait(self.CLOSE_BTN)
        # Ждём, пока модалка исчезнет
        self.wait_for_element_invisible(self.MODAL)
