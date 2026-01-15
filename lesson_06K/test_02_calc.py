from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestSlowCalculator:
    """Тест для медленного калькулятора"""
    
    @pytest.fixture(scope="function")
    def driver(self):
        """Фикстура для инициализации браузера Chrome"""
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()
    
    def test_slow_calculator(self, driver):
        """Тест медленного калькулятора с задержкой 45 секунд"""
        
        # 1. Открыть страницу в Google Chrome
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        print("✓ Страница калькулятора загружена")
        
        # 2. В поле ввода по локатору #delay ввести значение 45
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")
        print("✓ Задержка установлена: 45 секунд")
        
        # 3. Нажать на кнопки: 7 + 8 =
        # Получаем ВСЕ кнопки калькулятора для анализа
        all_buttons = driver.find_elements(By.CSS_SELECTOR, ".btn")
        print(f"Найдено кнопок: {len(all_buttons)}")
        
        # Создаем словарь для поиска кнопок по тексту
        buttons_dict = {}
        for btn in all_buttons:
            text = btn.text.strip()
            if text:
                buttons_dict[text] = btn
                print(f"  Кнопка: '{text}'")
        
        # Нажимаем кнопки в правильной последовательности
        buttons_to_click = ["7", "+", "8", "="]
        
        for button_text in buttons_to_click:
            if button_text in buttons_dict:
                buttons_dict[button_text].click()
                print(f"✓ Нажата кнопка: {button_text}")
            else:
                # Пробуем найти кнопку другими способами
                try:
                    # Ищем среди всех span элементов
                    spans = driver.find_elements(By.TAG_NAME, "span")
                    for span in spans:
                        if span.text.strip() == button_text and "btn" in span.get_attribute("class"):
                            span.click()
                            print(f"✓ Нажата кнопка (через span): {button_text}")
                            break
                except:
                    print(f"✗ Не удалось найти кнопку: {button_text}")
        
        # 4. Проверить (assert), что в окне отобразится результат 15 через 45 секунд
        # Находим экран калькулятора
        screen = driver.find_element(By.CSS_SELECTOR, ".screen")
        
        print("\n⏳ Ожидаем результат 45 секунд...")
        
        # Используем WebDriverWait с таймаутом 46 секунд (45 + запас)
        wait = WebDriverWait(driver, 46)
        
        # Ждем, пока на экране появится текст "15"
        try:
            wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
            )
        except:
            # Альтернативный способ: ждем любого непустого результата
            wait.until(
                lambda d: d.find_element(By.CSS_SELECTOR, ".screen").text.strip() != ""
            )
        
        # Получаем окончательный результат
        final_result = screen.text.strip()
        print(f"✓ Результат отобразился: '{final_result}'")
        
        # Проверяем assert
        assert final_result == "15", f"Ожидался результат 15, но получено: '{final_result}'"
        print("✅ Результат 15 получен корректно!")


# Запуск через pytest
if __name__ == "__main__":
    pytest.main([__file__, "-v"])