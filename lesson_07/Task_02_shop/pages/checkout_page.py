from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    """
    Page Object для страницы оформления заказа.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Локаторы для формы
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.cancel_button = (By.ID, "cancel")
        
        # Локаторы для страницы обзора заказа
        self.finish_button = (By.ID, "finish")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
        self.tax_label = (By.CLASS_NAME, "summary_tax_label")
    
    def fill_shipping_info(self, first_name, last_name, postal_code):
        """Заполнить форму данными для доставки."""
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
    
    def click_continue(self):
        """Нажать кнопку Continue после заполнения формы."""
        self.driver.find_element(*self.continue_button).click()
    
    def get_total_price(self):
        """Получить итоговую стоимость со страницы."""
        # Ждем пока страница загрузится и элемент станет видимым
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.total_label)
        )
        total_text = total_element.text
        
        # Извлекаем число из строки типа "Total: $58.29"
        if "Total: $" in total_text:
            price_str = total_text.split("Total: $")[1]
            try:
                return float(price_str)
            except ValueError:
                return None
        return None
    
    def click_finish(self):
        """Нажать кнопку Finish."""
        self.driver.find_element(*self.finish_button).click()