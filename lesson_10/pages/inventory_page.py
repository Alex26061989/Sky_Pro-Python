from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from typing import List, Dict


class InventoryPage(BasePage):
    """
    Класс для работы со страницей товаров.
    """
    
    # Локаторы
    CART_LINK: tuple = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE: tuple = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCT_ADD_BUTTON_TEMPLATE: str = "add-to-cart-{}"
    
    # Словарь соответствия названий товаров и их идентификаторов
    PRODUCT_IDS: Dict[str, str] = {
        "Sauce Labs Backpack": "sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt": "sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie": "sauce-labs-onesie"
    }
    
    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы товаров"""
        super().__init__(driver)
    
    def add_product_to_cart(self, product_name: str) -> None:
        """Добавить один товар в корзину по названию"""
        if product_name not in self.PRODUCT_IDS:
            raise ValueError(f"Товар '{product_name}' не найден")
        
        product_id = self.PRODUCT_IDS[product_name]
        add_button_locator = (
            By.ID, 
            self.PRODUCT_ADD_BUTTON_TEMPLATE.format(product_id)
        )
        self.click_element(add_button_locator)
    
    def add_products_to_cart(self, product_list: List[str]) -> None:
        """Добавить несколько товаров в корзину"""
        for product in product_list:
            self.add_product_to_cart(product)
    
    def go_to_cart(self) -> None:
        """Перейти в корзину"""
        self.click_element(self.CART_LINK)
    
    def get_cart_item_count(self) -> int:
        """Получить количество товаров в корзине"""
        if self.is_element_visible(self.CART_BADGE, timeout=2):
            badge_text = self.get_text(self.CART_BADGE)
            try:
                return int(badge_text)
            except ValueError:
                return 0
        return 0