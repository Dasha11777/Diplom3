
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage

class MainPage(BasePage):
    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BTN = (By.XPATH, "//p[contains(text(),'Лента') or text()='Лента заказов']")
    # Используем более универсальный локатор - все элементы с изображениями ингредиентов
    INGREDIENT_CARD = (By.XPATH, "//a[contains(@href, '/ingredient/')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//p[@class and contains(@class, 'counter')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    def open_main(self):
        self.open("https://stellarburgers.education-services.ru/")
        # Ждём загрузку страницы
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    def click_constructor(self):
        self.click(self.CONSTRUCTOR_BTN)

    def click_order_feed(self):
        self.click(self.ORDER_FEED_BTN)

    def click_ingredient(self, name):
        # Ждём загрузку ингредиентов
        self.wait.until(EC.presence_of_all_elements_located(self.INGREDIENT_CARD))
        time.sleep(1)
        cards = self.driver.find_elements(*self.INGREDIENT_CARD)
        for card in cards:
            try:
                if name in card.text:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", card)
                    time.sleep(0.5)
                    card.click()
                    return True
            except:
                continue
        return False

    def get_ingredient_counter(self, name):
        cards = self.driver.find_elements(*self.INGREDIENT_CARD)
        for card in cards:
            if name in card.text:
                try:
                    counter_elem = card.find_element(*self.INGREDIENT_COUNTER)
                    return int(counter_elem.text)
                except:
                    return 0
        return 0
