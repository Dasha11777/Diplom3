
import pytest
import allure
from pages.main_page import MainPage

@pytest.mark.usefixtures("driver_init")
@allure.feature("Навигация")
class TestNavigation:

    @allure.story("Переход по клику на Конструктор")
    def test_click_constructor(self):
        main = MainPage(self.driver)
        main.open_main()
        main.click_order_feed()  # Сначала перейти на ленту заказов
        main.click_constructor()  # Затем на конструктор
        assert "construct" in self.driver.current_url or "burger" in self.driver.current_url

    @allure.story("Переход по клику на раздел Лента заказов")
    def test_click_order_feed(self):
        main = MainPage(self.driver)
        main.open_main()
        main.click_order_feed()
        assert "feed" in self.driver.current_url
