from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object для страницы корзины"""
    
    # Локаторы
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def is_loaded(self):
        """Проверить, что страница корзины загрузилась"""
        try:
            self.wait.until(
                EC.presence_of_element_located(self.CHECKOUT_BUTTON)
            )
            return True
        except:
            return False
    
    def get_cart_items(self):
        """Получить все товары в корзине"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return [item.find_element(*self.ITEM_NAME).text for item in items]
    
    def get_cart_items_count(self):
        """Получить количество товаров в корзине"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    
    def click_checkout(self):
        """Нажать кнопку Checkout"""
        element = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        element.click()