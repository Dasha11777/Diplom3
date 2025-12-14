import allure
from pages.main_page import MainPage
from urls import Urls

@allure.feature("Навигация")
class TestNavigation:

    @allure.story("Переход по клику на Конструктор")
    def test_click_constructor(self, driver):
        main = MainPage(driver)
        main.open_main()
        main.click_order_feed()  # Сначала перейти на ленту заказов
        main.click_constructor()  # Затем на конструктор
        assert driver.current_url == Urls.BASE_URL

    @allure.story("Переход по клику на раздел Лента заказов")
    def test_click_order_feed(self, driver):
        main = MainPage(driver)
        main.open_main()
        main.click_order_feed()
        assert driver.current_url == Urls.BASE_URL + Urls.ORDER_FEED_PATH
