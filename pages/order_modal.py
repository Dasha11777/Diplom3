import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderModalPage(BasePage):
    MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__container')]")
    ORDER_NUMBER = (By.XPATH, "(//section[contains(@class,'Modal_modal_opened')])[last()]//h2[contains(@class,'text_type_digits-large')]")
    CLOSE_BUTTON = (By.XPATH, "(//section[contains(@class,'Modal_modal_opened')])[last()]//button[contains(@class,'Modal_modal__close')]")
    SUCCESS_ICON = (By.XPATH, "(//section[contains(@class,'Modal_modal_opened')])[last()]//img[contains(@alt,'tick') or contains(@src,'tick')]")
    LOADING_SPINNER = (By.XPATH, "//img[contains(@class,'Modal_modal__loading')]")

    @allure.step('Проверка открытия модального окна заказа')
    def is_open(self):
        # Проверяем текущее состояние модалки без ожидания
        elements = self.find_elements_now(self.MODAL)
        return len(elements) > 0 and elements[0].is_displayed()

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        # Сначала дожидаемся появления модального окна
        self.wait_for_visible_element(self.MODAL)

        # Ждем пока модалка станет активной и номер заказа станет актуальным
        self._wait_until_order_ready()
        self.wait_for_clickable_element(self.CLOSE_BUTTON)

        text = self.wait_for_visible_element(self.ORDER_NUMBER).text.strip()
        return text

    @allure.step('Закрытие модального окна заказа')
    def close(self):
        """Закрыть модальное окно заказа"""
        self.click_with_wait(self.CLOSE_BUTTON)

    # пришлось придумывать это из-за бага на сайте, когда у нас есть дефолтная 9999 модалка
    @allure.step('Ожидание готовности заказа в модальном окне')
    def _wait_until_order_ready(self):
        try:
            self.wait_for_visible_element(self.SUCCESS_ICON)
        except:
            pass

        try:
            self.wait_for_element_invisible(self.LOADING_SPINNER)
        except:
            pass
