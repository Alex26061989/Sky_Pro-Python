import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Импортируем классы Page Object
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestSauceDemo:
    """Тест для проверки функциональности интернет-магазина Sauce Demo."""
    
    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации и завершения работы драйвера Firefox."""
        # Настройка Firefox драйвера
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()
    
    def test_complete_purchase_flow(self, driver):
        """
        Полный тест потока покупки:
        1. Авторизация
        2. Добавление товаров в корзину
        3. Оформление заказа
        4. Проверка итоговой суммы
        """
        # 1. Открыть сайт магазина и авторизоваться
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        # 2. На главной странице добавляем товары в корзину
        inventory_page = InventoryPage(driver)
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt", 
            "Sauce Labs Onesie"
        ]
        inventory_page.add_products_to_cart(products_to_add)
        
        # 3. Переходим в корзину и нажимаем Checkout
        inventory_page.go_to_cart()
        
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        
        # 4. Заполняем форму оформления заказа
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_shipping_info("Иван", "Иванов", "123456")
        checkout_page.click_continue()
        
        # 5. Получаем и проверяем итоговую стоимость
        total_price = checkout_page.get_total_price()
        
        # 6. Проверка (assert)
        assert total_price == 58.29, f"Ожидалась сумма $58.29, но получено ${total_price}"
        
        # 7. Дополнительная проверка - можно также проверить количество товаров
        # (опционально, не требуется по заданию)
        
        print(f"✓ Тест пройден успешно! Итоговая сумма: ${total_price}")
        
        # 8. Закрытие браузера выполнится автоматически благодаря фикстуре
    
    def test_individual_steps(self, driver):
        """
        Альтернативный тест с более детальными шагами.
        Полезен для отладки, если полный тест не работает.
        """
        # Шаг 1: Авторизация
        login_page = LoginPage(driver)
        login_page.open()
        
        # Проверяем, что мы на странице логина
        assert "Swag Labs" in driver.title
        
        # Вводим учетные данные
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        
        # Проверяем, что авторизация прошла успешно
        assert "inventory" in driver.current_url
        
        # Шаг 2: Добавление товаров
        inventory_page = InventoryPage(driver)
        
        # Добавляем каждый товар по отдельности
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_product_to_cart("Sauce Labs Onesie")
        
        # Проверяем, что в корзине появился значок с количеством товаров
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "3"
        
        # Шаг 3: Переход в корзину
        inventory_page.go_to_cart()
        assert "cart" in driver.current_url
        
        # Шаг 4: Начало оформления заказа
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        assert "checkout-step-one" in driver.current_url
        
        # Шаг 5: Заполнение информации
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_shipping_info("Петр", "Петров", "654321")
        checkout_page.click_continue()
        assert "checkout-step-two" in driver.current_url
        
        # Шаг 6: Проверка итоговой суммы
        total = checkout_page.get_total_price()
        assert total == 58.29, f"Итоговая сумма неверная: ${total}"
        
        print(f"✓ Все шаги выполнены успешно! Итог: ${total}")