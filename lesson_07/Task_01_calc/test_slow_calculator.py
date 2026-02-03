import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage

class TestSlowCalculator:
    """Тест для проверки функциональности медленного калькулятора."""
    
    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации и завершения работы драйвера."""
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        yield driver
        driver.quit()
    
    def test_calculation_with_delay(self, driver):
        """
        Тест: ввод задержки 45 секунд, выполнение операции 7 + 8
        и проверка, что результат 15 отобразится через ожидаемое время.
        """
        # 1. Создание объекта страницы
        calc_page = CalculatorPage(driver)
        
        # 2. Открыть страницу калькулятора
        calc_page.open()
        
        # 3. Очистить экран (на всякий случай)
        calc_page.clear_screen()
        
        # 4. Ввести значение 45 в поле задержки
        calc_page.set_delay(45)
        
        # 5. Нажать кнопки: 7, +, 8, =
        calc_page.click_button('7')
        calc_page.click_button('+')
        calc_page.click_button('8')
        calc_page.click_button('=')
        
        # 6. Вариант 1: Использовать метод get_result()
        result = calc_page.get_result(timeout=46)  # Даем на 1 секунду больше задержки
        assert result == "15", f"Ожидался результат '15', но получено '{result}'"
        
        # 7. ИЛИ Вариант 2: Использовать метод wait_for_result()
        # success = calc_page.wait_for_result("15", timeout=46)
        # assert success, "Результат '15' не появился в течение заданного времени"
        
        print(f"✓ Тест пройден! Результат: {result}")
        
    def test_calculation_with_delay_alternative(self, driver):
        """
        Альтернативная версия теста с более простым подходом.
        """
        calc_page = CalculatorPage(driver)
        calc_page.open()
        calc_page.clear_screen()
        calc_page.set_delay(45)
        
        # Выполняем вычисление
        calc_page.click_button('7')
        calc_page.click_button('+')
        calc_page.click_button('8')
        calc_page.click_button('=')
        
        # Ждем пока на экране не появится что-то отличное от "7+8"
        # И проверяем что это именно "15"
        
        # Сначала получаем текущее выражение
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        
        # Ждем изменения текста с "7+8" на что-то другое
        wait = WebDriverWait(driver, 46)
        
        # Ожидаем пока текст не станет числом (проверяем что это не выражение)
        def is_result_ready(driver):
            text = driver.find_element(By.CSS_SELECTOR, ".screen").text
            # Результат готов если это число (не содержит операторов +-÷x)
            return text.isdigit() or (text.startswith('-') and text[1:].isdigit())
        
        wait.until(is_result_ready)
        
        # Получаем итоговый результат
        result = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result == "15", f"Ожидался результат '15', но получено '{result}'"
        print(f"✓ Альтернативный тест пройден! Результат: {result}")