import allure
from pages.main_page import MainPage
from pages.ingredient_modal import IngredientModalPage

@allure.feature("Всплывающее окно ингредиента")
class TestIngredientModal:

    @allure.story("Открытие модального окна ингредиента")
    def test_ingredient_modal_open(self, driver):
        main = MainPage(driver)
        main.open_main()

        ingredient_name = "Краторная булка"  # Один из известных ингредиентов
        main.click_ingredient(ingredient_name)

        modal = IngredientModalPage(driver)
        # Ждём, пока модалка откроется
        modal.wait_until_open()
        assert modal.is_open(), "Модальное окно не открылось"
        # Проверяем, что открылось окно именно с нужным ингредиентом
        actual_name = modal.get_ingredient_name()
        assert ingredient_name in actual_name, f"Открылось модальное окно не с тем ингредиентом. Ожидали ингредиент содержащий '{ingredient_name}', получили: '{actual_name}'"

    @allure.story("Закрытие модального окна ингредиента")
    def test_ingredient_modal_close(self, driver):
        main = MainPage(driver)
        main.open_main()

        ingredient_name = "Краторная булка"  # Один из известных ингредиентов
        main.click_ingredient(ingredient_name)

        modal = IngredientModalPage(driver)
        modal.wait_until_open()
        # Проверяем, что открылось окно именно с нужным ингредиентом
        actual_name = modal.get_ingredient_name()
        assert ingredient_name in actual_name, f"Открылось модальное окно не с тем ингредиентом. Ожидали ингредиент содержащий '{ingredient_name}', получили: '{actual_name}'"

        modal.close()  # Метод close уже ждёт закрытия
        assert not modal.is_open(), "Модальное окно не закрылось"
