from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    """
    Класс Page Object для страницы медленного калькулятора.
    Содержит локаторы и методы взаимодействия с элементами.
    """
    
    # Локаторы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")  # Основной экран калькулятора
    # Кнопки для простоты обращения
    BUTTONS = {
        '7': (By.XPATH, "//span[text()='7']"),
        '8': (By.XPATH, "//span[text()='8']"),
        '+': (By.XPATH, "//span[text()='+']"),
        '=': (By.XPATH, "//span[text()='=']"),
        'C': (By.XPATH, "//span[text()='C']"),  # Кнопка очистки
        # При необходимости можно добавить другие кнопки
    }
    
    def __init__(self, driver):
        """Инициализация драйвера."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)  # Увеличенный таймаут для медленного расчета
    
    def open(self):
        """Открыть страницу калькулятора."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, seconds):
        """Установить значение задержки в секундах."""
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(seconds))
    
    def click_button(self, button_label):
        """Нажать на кнопку калькулятора по её тексту (например, '7', '+', '=')."""
        button_locator = self.BUTTONS.get(button_label)
        if button_locator:
            self.driver.find_element(*button_locator).click()
        else:
            raise ValueError(f"Кнопка с текстом '{button_label}' не найдена в словаре BUTTONS")
    
    def clear_screen(self):
        """Очистить экран калькулятора."""
        self.click_button('C')
    
    def get_result(self, timeout=45):
        """
        Получить окончательный результат с экрана калькулятора.
        Ожидает, пока выражение (например, '7+8') не заменится числовым результатом.
        
        Args:
            timeout: максимальное время ожидания в секундах
            
        Returns:
            str: итоговый результат вычисления
        """
        # Ожидаем, что текст на экране изменится с выражения на результат
        # Для этого сначала получаем текущее выражение
        current_text = self.driver.find_element(*self.RESULT_SCREEN).text
        
        # Ждем, пока текст не станет отличным от текущего выражения
        # и не будет пустым (на случай, если экран очистится)
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*self.RESULT_SCREEN).text != current_text 
            and driver.find_element(*self.RESULT_SCREEN).text != ""
        )
        
        # Возвращаем новый текст (результат)
        return self.driver.find_element(*self.RESULT_SCREEN).text
    
    def wait_for_result(self, expected_result, timeout=45):
        """
        Альтернативный метод: ждет появления конкретного результата.
        
        Args:
            expected_result: ожидаемый результат (например, "15")
            timeout: максимальное время ожидания в секундах
            
        Returns:
            bool: True если результат появился вовремя
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(self.RESULT_SCREEN, expected_result)
            )
            return True
        except:
            return False