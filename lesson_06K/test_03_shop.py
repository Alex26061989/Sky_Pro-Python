from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestOnlineShop:
    """Тест для интернет-магазина"""
    
    @pytest.fixture(scope="function")
    def driver(self):
        """Фикстура для инициализации браузера Firefox"""
        driver = webdriver.Firefox()
        driver.maximize_window()
        yield driver
        driver.quit()
    
    def test_online_shop(self, driver):
        """Тест добавления товаров в корзину в интернет-магазине"""
        
        # 1. Открыть страницу в Firefox
        driver.get("https://www.saucedemo.com/")
        print("✓ Страница магазина загружена")
        
        # 2. Авторизоваться как пользователь 'standard_user'
        username_field = driver.find_element(By.ID, "user-name")
        username_field.send_keys("standard_user")
        print("✓ Введен логин: standard_user")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")
        print("✓ Введен пароль")
        
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        print("✓ Выполнен вход в систему")
        
        # Ждем загрузки страницы с товарами
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
        print("✓ Страница с товарами загружена")
        
        # 3. Добавить в корзину товары 'Sauce Labs Backpack' и 'Sauce Labs Bolt T-Shirt'
        # Находим все товары
        inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"✓ Найдено товаров: {len(inventory_items)}")
        
        # Словарь для хранения кнопок добавления товаров
        add_to_cart_buttons = {}
        
        for item in inventory_items:
            item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            add_button = item.find_element(By.CSS_SELECTOR, "button.btn_inventory")
            add_to_cart_buttons[item_name] = add_button
            print(f"  Товар: {item_name}")
        
        # Добавляем нужные товары в корзину
        items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt"]
        
        for item_name in items_to_add:
            if item_name in add_to_cart_buttons:
                add_to_cart_buttons[item_name].click()
                print(f"✓ Добавлен в корзину: {item_name}")
            else:
                print(f"✗ Товар не найден: {item_name}")
        
        # 4. Перейти в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        print("✓ Перешли в корзину")
        
        # Ждем загрузки корзины
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        
        # 5. Проверить, что в корзине ровно 2 товара
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        cart_items_count = len(cart_items)
        
        print(f"✓ Товаров в корзине: {cart_items_count}")
        assert cart_items_count == 2, f"В корзине должно быть 2 товара, но найдено: {cart_items_count}"
        
        # 6. Проверить названия товаров в корзине
        cart_item_names = []
        for item in cart_items:
            item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            cart_item_names.append(item_name)
            print(f"  В корзине: {item_name}")
        
        # Проверяем, что оба нужных товара в корзине
        for expected_item in items_to_add:
            assert expected_item in cart_item_names, f"Товар {expected_item} отсутствует в корзине"
        
        print("✓ Оба товара присутствуют в корзине")
        
        # 7. Нажать Checkout
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()
        print("✓ Нажата кнопка Checkout")
        
        # 8. Заполнить форму своими данными
        # Ждем загрузки формы
        wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        
        # Заполняем форму
        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "postal-code": "123456"
        }
        
        for field_id, value in form_data.items():
            field = driver.find_element(By.ID, field_id)
            field.clear()
            field.send_keys(value)
            print(f"✓ Заполнено поле {field_id}: {value}")
        
        # 9. Нажать Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        print("✓ Нажата кнопка Continue")
        
        # 10. Проверить итоговую сумму ($0 не учитывается)
        # Ждем загрузки страницы с итогом
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        
        # Находим элемент с общей суммой
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        print(f"✓ Итоговая сумма: {total_text}")
        
        # Извлекаем сумму из текста (формат: "Total: $XX.XX")
        import re
        total_match = re.search(r'\$(\d+\.\d+)', total_text)
        
        if total_match:
            total_amount = float(total_match.group(1))
            print(f"✓ Сумма заказа: ${total_amount}")
            
            # Проверяем, что сумма больше 0
            assert total_amount > 0, f"Итоговая сумма должна быть больше $0, но равна: ${total_amount}"
            
            # Проверяем, что сумма корректно рассчитана
            # Находим все суммы товаров
            item_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
            subtotal = 0.0
            
            for price_element in item_prices:
                price_text = price_element.text.replace('$', '')
                subtotal += float(price_text)
            
            # Добавляем налог (примерно 8%)
            tax = subtotal * 0.08
            expected_total = subtotal + tax
            
            # Проверяем с небольшой погрешностью
            assert abs(total_amount - expected_total) < 0.01, \
                f"Итоговая сумма некорректна. Ожидалось: ${expected_total:.2f}, получено: ${total_amount}"
            
            print(f"✓ Сумма рассчитана корректно: ${subtotal:.2f} + налог = ${expected_total:.2f}")
        
        else:
            print("⚠ Не удалось извлечь сумму из текста")
        
        print("\n" + "="*50)
        print("✅ ТЕСТ ПРОЙДЕН УСПЕШНО!")
        print("="*50)


# Запуск через pytest
if __name__ == "__main__":
    pytest.main([__file__, "-v"])