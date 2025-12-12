
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderModal(BasePage):
    MODAL = (By.CLASS_NAME, "Modal_modal__container__X7MgQ")
    ORDER_NUMBER = (By.CLASS_NAME, "OrderDetails_order_number__3DZMQ")

    def is_open(self):
        return len(self.driver.find_elements(*self.MODAL)) > 0

    def get_order_number(self):
        return self.find(self.ORDER_NUMBER).text
