import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from helpers.steps import (
    login,
    add_products_to_cart,
    go_to_cart_and_checkout,
    fill_shipping_info,
    verify_total_price
)


@allure.feature("Интернет-магазин")
@allure.story("Полный цикл покупки")
class TestSauceDemo:
    """Тесты для проверки функциональности интернет-магазина."""
    
    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации драйвера Firefox."""
        with allure.step("Инициализация Firefox драйвера"):
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
            driver.maximize_window()
        
        yield driver
        
        with allure.step("Закрытие браузера"):
            driver.quit()
    
    @allure.title("Тест полного цикла покупки")
    @allure.description("""
        Тест проверяет:
        1. Авторизацию под стандартным пользователем
        2. Добавление трёх товаров в корзину
        3. Оформление заказа
        4. Проверку итоговой суммы ($58.29)
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("smoke", "purchase")
    @allure.link("https://www.saucedemo.com", name="Сайт магазина")
    def test_complete_purchase_flow(self, driver):
        """Полный тест потока покупки."""
        
        login(driver, "standard_user", "secret_sauce")
        add_products_to_cart(
            driver, 
            ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        )
        go_to_cart_and_checkout(driver)
        fill_shipping_info(driver, "Иван", "Иванов", "123456")
        verify_total_price(driver, 58.29)