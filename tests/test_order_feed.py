import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_modal import OrderModalPage
from test_data import IngredientData

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.story("Счётчики выполненных заказов увеличиваются после создания заказа")
    @allure.title("Проверка увеличения счётчиков 'Выполнено за всё время' и 'Выполнено за сегодня'")
    def test_order_counters_increase(self, driver, authorized_user):
        main = MainPage(driver)
        main.open_main()
        main.click_order_feed()

        feed = OrderFeedPage(driver)
        done_all_time_before = feed.get_done_all_time()
        done_today_before = feed.get_done_today()

        # Для создания заказа обязательно зайти на конструктор и оформить заказ
        main.click_constructor()

        # Добавляем ингредиенты
        main.add_ingredient_to_constructor(IngredientData.CRATER_BUN['name'])
        main.add_ingredient_to_constructor(IngredientData.BEEF_METEORITE['name'])
        
        # Оформляем заказ
        main.click_order_button()
        
        main.click_order_feed()

        done_all_time_after = feed.get_done_all_time()
        done_today_after = feed.get_done_today()

        assert done_all_time_after > done_all_time_before
        assert done_today_after > done_today_before

    @allure.story("Номер нового заказа появляется в разделе В работе")
    @allure.title("Проверка появления номера нового заказа в разделе 'В работе'")
    def test_order_number_in_progress(self, driver, authorized_user):
        main = MainPage(driver)
        main.open_main()
        main.click_constructor()
        
        # Добавляем булку и начинку
        main.add_ingredient_to_constructor(IngredientData.CRATER_BUN['name'])
        main.add_ingredient_to_constructor(IngredientData.BEEF_METEORITE['name'])
                
        # Оформляем заказ
        main.click_order_button()
        
        # Получаем номер заказа из модального окна
        order_modal = OrderModalPage(driver)
        order_number = order_modal.get_order_number()
        
        # Закрываем модальное окно
        order_modal.close()
        
        # Переходим в ленту заказов
        main.click_order_feed()
        
        feed = OrderFeedPage(driver)
        orders_in_progress = feed.get_in_progress_orders_numbers()

        # Проверяем, что номер заказа есть в списке "В работе"
        assert order_number in orders_in_progress, f"Номер заказа {order_number} не найден в разделе 'В работе'. Найдены: {orders_in_progress}"
