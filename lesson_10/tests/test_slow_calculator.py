import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


@allure.feature("Калькулятор")
@allure.story("Медленные вычисления")
class TestSlowCalculator:
    """Тесты для проверки функциональности медленного калькулятора."""
    
    @pytest.fixture
    def driver(self):
        """
        Фикстура для инициализации и завершения работы драйвера Chrome.
        Используем прямой путь к ChromeDriver вместо менеджера.
        """
        with allure.step("Инициализация Chrome драйвера"):
            # Пробуем разные варианты
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            
            try:
                # Сначала пробуем без указания сервиса (если chromedriver в PATH)
                driver = webdriver.Chrome(options=chrome_options)
            except:
                try:
                    # Если не получилось, пробуем с менеджером
                    from selenium.webdriver.chrome.service import Service as ChromeService
                    from webdriver_manager.chrome import ChromeDriverManager
                    service = ChromeService(ChromeDriverManager().install())
                    driver = webdriver.Chrome(service=service, options=chrome_options)
                except:
                    # Если всё сломалось, пропускаем тест
                    pytest.skip("ChromeDriver не установлен")
            
            driver.maximize_window()
        
        yield driver
        
        with allure.step("Закрытие браузера"):
            driver.quit()
    
    @allure.title("Тест сложения 7 + 8 с задержкой 45 секунд")
    @allure.description("Проверка работы медленного калькулятора")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("slow", "calculator")
    def test_calculation_with_delay(self, driver):
        """Тест проверяет работу калькулятора с задержкой."""
        
        from calculator_page import CalculatorPage
        from helpers.steps_calculator import (
            open_calculator,
            set_calculator_delay,
            perform_calculation,
            verify_calculation_result
        )
        
        calc_page = open_calculator(driver)
        set_calculator_delay(calc_page, 45)
        perform_calculation(calc_page, "7+8=")
        verify_calculation_result(calc_page, "15", timeout=46)