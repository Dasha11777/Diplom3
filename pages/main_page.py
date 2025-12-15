import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import Urls

class MainPage(BasePage):
    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BTN = (By.XPATH, "//p[contains(text(),'Лента') or text()='Лента заказов']")

    INGREDIENT_CARD = (By.XPATH, "//a[contains(@href, '/ingredient/')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//p[@class and contains(@class, 'counter')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Область конструктора бургера
    BURGER_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")

    @allure.step('Открытие главной страницы')
    def open_main(self):
        self.open(Urls.BASE_URL)
        # Ждём загрузку ингредиентов как признак полной загрузки страницы
        self.wait_for_elements_in_dom(self.INGREDIENT_CARD)
    
    @allure.step('Клик на кнопку Конструктор')
    def click_constructor(self):
        self.click_with_wait(self.CONSTRUCTOR_BTN)

    @allure.step('Клик на кнопку Лента заказов')
    def click_order_feed(self):
        self.click_with_wait(self.ORDER_FEED_BTN)

    @allure.step('Клик на ингредиент: {name}')
    def click_ingredient(self, name):
        # Создаём точный локатор для конкретного ингредиента по имени
        ingredient_locator = (By.XPATH, f"//a[contains(@href, '/ingredient/') and contains(., '{name}')]")
        # Прокручиваем к элементу перед кликом
        element = self.wait_for_visible_element(ingredient_locator)
        self.execute_script("arguments[0].scrollIntoView(true);", element)
        self.click_with_wait(ingredient_locator)

    @allure.step('Получение счетчика ингредиента: {name}')
    def get_ingredient_counter(self, name):
        # Создаём точный локатор для конкретного ингредиента по имени
        ingredient_locator = (By.XPATH, f"//a[contains(@href, '/ingredient/') and contains(., '{name}')]")
        card = self.find_element_now(ingredient_locator)
        try:
            counter_elem = card.find_element(*self.INGREDIENT_COUNTER)
            return int(counter_elem.text)
        except:
            return 0

    @allure.step('Добавление ингредиента "{name}" в конструктор')
    def add_ingredient_to_constructor(self, name):
        """Перетащить ингредиент в конструктор бургера"""
        # Создаём локатор для конкретного ингредиента по имени
        ingredient_locator = (By.XPATH, f"//a[contains(@href, '/ingredient/') and contains(., '{name}')]")
        # Прокручиваем к ингредиенту перед перетаскиванием
        element = self.wait_for_visible_element(ingredient_locator)
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        # Перетаскиваем ингредиент в конструктор
        self.drag_and_drop(ingredient_locator, self.BURGER_CONSTRUCTOR)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_order_button(self):
        """Кликнуть на кнопку оформления заказа"""
        self.click_with_wait(self.ORDER_BUTTON)
