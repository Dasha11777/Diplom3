import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    DONE_ALL_TIME_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за всё время')]/following-sibling::p | //p[contains(text(),'Выполнено за все время')]/following-sibling::p")
    DONE_TODAY_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    IN_PROGRESS_SECTION = (By.XPATH, "//p[contains(text(),'В работе')]/following-sibling::ul")
    IN_PROGRESS_ORDERS = (By.XPATH, "//p[contains(text(),'В работе')]/following-sibling::ul//li")

    @allure.step('Получение количества заказов выполненных за всё время')
    def get_done_all_time(self):
        return int(self.wait_for_visible_element(self.DONE_ALL_TIME_COUNTER).text)

    @allure.step('Получение количества заказов выполненных за сегодня')
    def get_done_today(self):
        return int(self.wait_for_visible_element(self.DONE_TODAY_COUNTER).text)

    @allure.step('Получение номеров заказов в работе')
    def get_in_progress_orders_numbers(self):
        # Ждем, пока секция "В работе" загрузится
        self.wait_for_visible_element(self.IN_PROGRESS_SECTION)
        
        # Получаем все элементы заказов
        elems = self.find_elements_now(self.IN_PROGRESS_ORDERS)
        # Извлекаем только цифры из текста (убираем #)
        return [elem.text.replace('#', '').strip() for elem in elems if elem.text]
