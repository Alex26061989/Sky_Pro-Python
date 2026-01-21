from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для страницы калькулятора"""
    
    # Локаторы элементов
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CLASS_NAME, "screen")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        """Открыть страницу калькулятора"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, delay_seconds):
        """Установить задержку вычислений"""
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))
    
    def click_button(self, button_text):
        """Нажать кнопку калькулятора"""
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()
    
    def click_7(self):
        """Нажать кнопку 7"""
        self.click_button("7")
    
    def click_plus(self):
        """Нажать кнопку +"""
        self.click_button("+")
    
    def click_8(self):
        """Нажать кнопку 8"""
        self.click_button("8")
    
    def click_equals(self):
        """Нажать кнопку ="""
        self.click_button("=")
    
    def get_screen_text(self):
        """Получить текст с экрана калькулятора"""
        screen = self.wait.until(
            EC.presence_of_element_located(self.SCREEN)
        )
        return screen.text
    
    def wait_for_result(self, expected_result, timeout=46):
        """Подождать появления результата на экране"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(
                EC.text_to_be_present_in_element(self.SCREEN, expected_result)
            )
        except:
            return False