import allure
from pages.main_page import MainPage
from test_data import IngredientData

@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.story("Увеличивается счётчик булки при добавлении")
    @allure.title("Проверка увеличения счётчика булки на 2 при добавлении")
    def test_bun_counter_increment(self, driver):
        main = MainPage(driver)
        main.open_main()

        ingredient_name = IngredientData.CRATER_BUN['name']
        initial_count = main.get_ingredient_counter(ingredient_name)
        
        main.add_ingredient_to_constructor(ingredient_name)

        count_after = main.get_ingredient_counter(ingredient_name)
        assert count_after == initial_count + 2, f"Счётчик булки должен увеличиться на 2 (было {initial_count}, стало {count_after})"

    @allure.story("Увеличивается счётчик начинки при добавлении")
    @allure.title("Проверка увеличения счётчика начинки на 1 при добавлении")
    def test_filling_counter_increment(self, driver):
        main = MainPage(driver)
        main.open_main()

        ingredient_name = IngredientData.BEEF_METEORITE['name']
        initial_count = main.get_ingredient_counter(ingredient_name)
        
        main.add_ingredient_to_constructor(ingredient_name)

        count_after = main.get_ingredient_counter(ingredient_name)
        assert count_after == initial_count + 1, f"Счётчик начинки должен увеличиться на 1 (было {initial_count}, стало {count_after})"

