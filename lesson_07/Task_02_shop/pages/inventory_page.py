from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    """
    Page Object для главной страницы магазина.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Локаторы для товаров (используем data-test атрибуты)
        self.product_add_button = "add-to-cart-{}"
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        
        # Словарь соответствия названий товаров и их идентификаторов
        self.product_ids = {
            "Sauce Labs Backpack": "sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "sauce-labs-onesie"
        }
    
    def add_product_to_cart(self, product_name):
        """
        Добавить товар в корзину по названию.
        
        Args:
            product_name: название товара из словаря product_ids
        """
        if product_name in self.product_ids:
            product_id = self.product_ids[product_name]
            add_button_locator = (By.ID, self.product_add_button.format(product_id))
            self.driver.find_element(*add_button_locator).click()
        else:
            raise ValueError(f"Товар '{product_name}' не найден в списке доступных товаров")
    
    def add_products_to_cart(self, product_list):
        """Добавить несколько товаров в корзину."""
        for product in product_list:
            self.add_product_to_cart(product)
    
    def go_to_cart(self):
        """Перейти в корзину."""
        self.driver.find_element(*self.cart_link).click()