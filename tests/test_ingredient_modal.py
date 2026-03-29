import allure
import pytest
from pages.main_page import MainPage
from pages.ingredient_modal import IngredientModalPage
from test_data import IngredientData

@allure.feature("Всплывающее окно ингредиента")
class TestIngredientModal:

    @allure.story("Открытие модального окна ингредиента")
    @allure.title("Проверка открытия модального окна ингредиента при клике")
    @pytest.mark.parametrize('ingredient', [
        IngredientData.CRATER_BUN,
        IngredientData.BEEF_METEORITE
    ], ids=['булка', 'начинка'])
    def test_ingredient_modal_open(self, driver, ingredient):
        main = MainPage(driver)
        main.open_main()

        main.click_ingredient(ingredient['name'])

        modal = IngredientModalPage(driver)
        # Ждём, пока модалка откроется
        modal.wait_until_open()
        assert modal.is_open(), "Модальное окно не открылось"
        
        # Проверяем URL - должен измениться на /ingredient/{id}
        assert "/ingredient/" in driver.current_url, "URL не изменился на страницу ингредиента"
        
        # Проверяем название ингредиента
        actual_name = modal.get_ingredient_name()
        assert ingredient['full_name'] == actual_name, f"Неверное название ингредиента. Ожидали: '{ingredient['full_name']}', получили: '{actual_name}'"
        
        # Проверяем наличие изображения
        assert modal.has_image(), "Изображение ингредиента отсутствует"
        
        # Проверяем пищевую ценность
        assert modal.get_calories() == ingredient['calories'], f"Неверная калорийность. Ожидали: '{ingredient['calories']}', получили: '{modal.get_calories()}'"
        assert modal.get_proteins() == ingredient['proteins'], f"Неверное количество белков. Ожидали: '{ingredient['proteins']}', получили: '{modal.get_proteins()}'"
        assert modal.get_fats() == ingredient['fats'], f"Неверное количество жиров. Ожидали: '{ingredient['fats']}', получили: '{modal.get_fats()}'"
        assert modal.get_carbs() == ingredient['carbs'], f"Неверное количество углеводов. Ожидали: '{ingredient['carbs']}', получили: '{modal.get_carbs()}'"

    @allure.story("Закрытие модального окна ингредиента")
    @allure.title("Проверка закрытия модального окна ингредиента по клику на крестик")
    def test_ingredient_modal_close(self, driver):
        main = MainPage(driver)
        main.open_main()

        ingredient = IngredientData.CRATER_BUN
        main.click_ingredient(ingredient['name'])

        modal = IngredientModalPage(driver)
        modal.wait_until_open()
        # Проверяем, что открылось окно именно с нужным ингредиентом
        actual_name = modal.get_ingredient_name()
        assert ingredient['full_name'] == actual_name, f"Открылось модальное окно не с тем ингредиентом. Ожидали '{ingredient['full_name']}', получили: '{actual_name}'"

        modal.close()  # Метод close уже ждёт закрытия
        assert not modal.is_open(), "Модальное окно не закрылось"
