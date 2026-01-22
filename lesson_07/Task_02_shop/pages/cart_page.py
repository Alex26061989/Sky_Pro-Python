from selenium.webdriver.common.by import By

class CartPage:
    """
    Page Object для страницы корзины.
    """
    
    def __init__(self, driver):
        self.driver = driver
        
        # Локаторы
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.continue_shopping_button = (By.ID, "continue-shopping")
    
    def click_checkout(self):
        """Нажать кнопку Checkout."""
        self.driver.find_element(*self.checkout_button).click()
    
    def get_cart_items_count(self):
        """Получить количество товаров в корзине."""
        items = self.driver.find_elements(*self.cart_items)
        return len(items)