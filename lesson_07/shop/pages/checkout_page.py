from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа"""
    
    # Локаторы для формы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    
    # Локаторы для итоговой страницы
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def is_loaded(self):
        """Проверить, что страница оформления загрузилась"""
        try:
            self.wait.until(
                EC.presence_of_element_located(self.FIRST_NAME_INPUT)
            )
            return True
        except:
            return False
    
    def fill_form(self, first_name, last_name, postal_code):
        """Заполнить форму данными"""
        # Ввести имя
        element = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        element.clear()
        element.send_keys(first_name)
        
        # Ввести фамилию
        element = self.driver.find_element(*self.LAST_NAME_INPUT)
        element.clear()
        element.send_keys(last_name)
        
        # Ввести почтовый индекс
        element = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        element.clear()
        element.send_keys(postal_code)
    
    def click_continue(self):
        """Нажать Continue"""
        element = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        element.click()
    
    def get_total_amount(self):
        """Получить итоговую стоимость (текст)"""
        self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        element = self.driver.find_element(*self.TOTAL_LABEL)
        return element.text
    
    def extract_total_value(self):
        """Извлечь числовое значение итоговой суммы"""
        total_text = self.get_total_amount()
        # Формат: "Total: $58.29"
        import re
        match = re.search(r'\$([\d.]+)', total_text)
        if match:
            return float(match.group(1))
        return 0.0