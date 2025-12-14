
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import Urls

class MainPage(BasePage):
    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BTN = (By.XPATH, "//p[contains(text(),'Лента') or text()='Лента заказов']")
    # Используем более универсальный локатор - все элементы с изображениями ингредиентов
    INGREDIENT_CARD = (By.XPATH, "//a[contains(@href, '/ingredient/')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//p[@class and contains(@class, 'counter')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    def open_main(self):
        self.open(Urls.BASE_URL)
        # Ждём загрузку ингредиентов как признак полной загрузки страницы
        self.wait_for_elements_in_dom(self.INGREDIENT_CARD)
    
    def click_constructor(self):
        self.click_with_wait(self.CONSTRUCTOR_BTN)

    def click_order_feed(self):
        self.click_with_wait(self.ORDER_FEED_BTN)

    def click_ingredient(self, name):
        # Создаём точный локатор для конкретного ингредиента по имени
        ingredient_locator = (By.XPATH, f"//a[contains(@href, '/ingredient/') and contains(., '{name}')]")
        # Прокручиваем к элементу перед кликом
        element = self.wait_for_visible_element(ingredient_locator)
        self.execute_script("arguments[0].scrollIntoView(true);", element)
        self.click_with_wait(ingredient_locator)

    def get_ingredient_counter(self, name):
        # Создаём точный локатор для конкретного ингредиента по имени
        ingredient_locator = (By.XPATH, f"//a[contains(@href, '/ingredient/') and contains(., '{name}')]")
        card = self.find_element_now(ingredient_locator)
        try:
            counter_elem = card.find_element(*self.INGREDIENT_COUNTER)
            return int(counter_elem.text)
        except:
            return 0
