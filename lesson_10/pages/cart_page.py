from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from typing import List


class CartPage(BasePage):
    """
    Класс для работы со страницей корзины.
    """
    
    # Локаторы
    CHECKOUT_BUTTON: tuple = (By.ID, "checkout")
    CART_ITEMS: tuple = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BUTTON: tuple = (By.ID, "continue-shopping")
    
    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы корзины"""
        super().__init__(driver)
    
    def click_checkout(self) -> None:
        """Нажать кнопку Checkout"""
        self.click_element(self.CHECKOUT_BUTTON)
    
    def get_cart_items_count(self) -> int:
        """Получить количество товаров в корзине"""
        items = self.find_elements(self.CART_ITEMS)
        return len(items)
    
    def get_cart_items(self) -> List:
        """Получить список всех товаров в корзине"""
        return self.find_elements(self.CART_ITEMS)
    
    def continue_shopping(self) -> None:
        """Вернуться к покупкам"""
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)