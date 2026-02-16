from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from typing import Optional


class CheckoutPage(BasePage):
    """
    Класс для работы со страницей оформления заказа.
    """
    
    # Локаторы для формы ввода данных
    FIRST_NAME_INPUT: tuple = (By.ID, "first-name")
    LAST_NAME_INPUT: tuple = (By.ID, "last-name")
    POSTAL_CODE_INPUT: tuple = (By.ID, "postal-code")
    CONTINUE_BUTTON: tuple = (By.ID, "continue")
    
    # Локаторы для страницы обзора заказа
    FINISH_BUTTON: tuple = (By.ID, "finish")
    TOTAL_LABEL: tuple = (By.CLASS_NAME, "summary_total_label")
    
    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы оформления заказа"""
        super().__init__(driver, timeout=10)
    
    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Заполнить форму данными для доставки"""
        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.POSTAL_CODE_INPUT, postal_code)
    
    def click_continue(self) -> None:
        """Нажать кнопку Continue"""
        self.click_element(self.CONTINUE_BUTTON)
    
    def click_finish(self) -> None:
        """Подтвердить заказ"""
        self.click_element(self.FINISH_BUTTON)
    
    def get_total_price(self) -> Optional[float]:
        """Получить итоговую стоимость"""
        try:
            total_text = self.get_text(self.TOTAL_LABEL, timeout=10)
            if "Total: $" in total_text:
                price_str = total_text.split("Total: $")[1]
                return float(price_str)
            return None
        except (ValueError, IndexError, AttributeError):
            return None