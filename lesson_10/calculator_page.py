from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Dict, Optional


class CalculatorPage:
    """
    Класс для работы со страницей медленного калькулятора.
    """
    
    # Локаторы
    DELAY_INPUT: tuple = (By.CSS_SELECTOR, "#delay")
    RESULT_SCREEN: tuple = (By.CSS_SELECTOR, ".screen")
    
    # Словарь с локаторами кнопок
    BUTTONS: Dict[str, tuple] = {
        '7': (By.XPATH, "//span[text()='7']"),
        '8': (By.XPATH, "//span[text()='8']"),
        '+': (By.XPATH, "//span[text()='+']"),
        '=': (By.XPATH, "//span[text()='=']"),
        'C': (By.XPATH, "//span[text()='C']"),
    }
    
    def __init__(self, driver: WebDriver, default_timeout: int = 60) -> None:
        """
        Инициализация страницы калькулятора
        
        Args:
            driver: экземпляр веб-драйвера
            default_timeout: стандартное время ожидания
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, default_timeout)
    
    def open(self) -> None:
        """Открыть страницу калькулятора"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, seconds: int) -> None:
        """Установить значение задержки в секундах"""
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(seconds))
    
    def click_button(self, button_label: str) -> None:
        """Нажать на кнопку калькулятора по её тексту"""
        button_locator = self.BUTTONS.get(button_label)
        if button_locator:
            self.driver.find_element(*button_locator).click()
        else:
            raise ValueError(f"Кнопка '{button_label}' не найдена")
    
    def clear_screen(self) -> None:
        """Очистить экран калькулятора"""
        self.click_button('C')
    
    def get_current_display(self) -> str:
        """Получить текущее отображаемое значение на экране"""
        return self.driver.find_element(*self.RESULT_SCREEN).text
    
    def get_result(self, timeout: int = 45) -> str:
        """Получить окончательный результат с экрана калькулятора"""
        current_text = self.get_current_display()
        
        WebDriverWait(self.driver, timeout).until(
            lambda driver: (
                self.get_current_display() != current_text 
                and self.get_current_display() != ""
            )
        )
        
        return self.get_current_display()
    
    def wait_for_result(self, expected_result: str, timeout: int = 45) -> bool:
        """Ожидание появления конкретного результата на экране"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(self.RESULT_SCREEN, expected_result)
            )
            return True
        except:
            return False