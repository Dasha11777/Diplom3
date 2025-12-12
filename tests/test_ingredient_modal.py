
import pytest
import allure
import time
from pages.main_page import MainPage
from pages.ingredient_modal import IngredientModal

@pytest.mark.usefixtures("driver_init")
@allure.feature("Всплывающее окно ингредиента")
class TestIngredientModal:

    @allure.story("Открытие и закрытие модального окна ингредиента")
    def test_ingredient_modal_open_close(self):
        main = MainPage(self.driver)
        main.open_main()

        ingredient_name = "Краторная булка"  # Один из известных ингредиентов
        opened = main.click_ingredient(ingredient_name)
        assert opened, "Не удалось кликнуть на ингредиент"

        modal = IngredientModal(self.driver)
        assert modal.is_open(), "Модальное окно не открылось"
        # Проверяем, что заголовок не пустой (модалка открылась правильно)
        title = modal.get_title()
        assert title and len(title) > 0, "Заголовок модального окна пустой"

        modal.close()
        time.sleep(1)  # Даём время на анимацию закрытия
        assert not modal.is_open(), "Модальное окно не закрылось"
