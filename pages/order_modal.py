
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderModalPage(BasePage):
    MODAL = (By.CLASS_NAME, "Modal_modal__container__X7MgQ")
    ORDER_NUMBER = (By.CLASS_NAME, "OrderDetails_order_number__3DZMQ")

    def is_open(self):
        # Проверяем текущее состояние модалки без ожидания
        elements = self.find_elements_now(self.MODAL)
        return len(elements) > 0 and elements[0].is_displayed()

    def get_order_number(self):
        return self.get_text_with_wait(self.ORDER_NUMBER)
