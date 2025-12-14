
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    # Более гибкие локаторы для счетчиков
    DONE_ALL_TIME_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за всё время')]/following-sibling::p | //p[contains(text(),'Выполнено за все время')]/following-sibling::p")
    DONE_TODAY_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    IN_PROGRESS_SECTION = (By.XPATH, "//p[contains(text(),'В работе')]/following-sibling::div")
    IN_PROGRESS_ORDERS = (By.XPATH, "//p[contains(text(),'В работе')]/following-sibling::div//li")

    def get_done_all_time(self):
        return int(self.wait_for_visible_element(self.DONE_ALL_TIME_COUNTER).text)

    def get_done_today(self):
        return int(self.wait_for_visible_element(self.DONE_TODAY_COUNTER).text)

    def get_in_progress_orders_numbers(self):
        elems = self.find_elements_now(self.IN_PROGRESS_ORDERS)
        return [elem.text for elem in elems]
